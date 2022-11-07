import uuid
import random
import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

from multiselectfield import MultiSelectField
from model_utils import FieldTracker

COLLECTIBLE_TIERS = (
    ('TIER_1', 'Legendary'),
    ('TIER_2', 'Epic'),
    ('TIER_3', 'Rare'),
    ('TIER_4', 'Uncommon'),
    ('TIER_5', 'Common'),
)

class Player(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    @property
    def username(self):
        return self.account.username
    
    def __str__(self) -> str:
        return self.username
    profile_image = models.ImageField(upload_to='images', default=None, null=True, blank=True)

    spacebucks = models.FloatField(default=10.0)
    coins = models.BigIntegerField(default=1000)

    @property
    def collectibles(self):
        return NFTCollectible.objects.filter(owner=self)

class PurchaseRequest(models.Model):
    nft_token = models.CharField(max_length=100, editable=False, unique=True)
    sender = models.ForeignKey(Player, default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='sender')
    receiver = models.ForeignKey(Player, default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='receiver')
    datetime_sent = models.DateTimeField(auto_now_add=True)

    amount = models.FloatField(default=0.0)
    
    is_accepted = models.BooleanField(default=False)
    datetime_accepted = models.DateTimeField(null=True, blank=True)

    tracker = FieldTracker()
    
    def __str__(self):
        return f"{self.sender} wants to buy {self.nft} from {self.receiver}"

@receiver(pre_save, sender=PurchaseRequest)
def pre_save_callback(sender, instance, *args, **kwargs):
    print('Pre save function...')
    if instance.tracker.has_changed('is_accepted') and instance.is_accepted:
        instance.datetime_accepted = datetime.datetime.now()
        instance.nft.owner = instance.sender
        instance.nft.save()

class NFTCollectible(models.Model):
    token = models.CharField(max_length=100, editable=False, unique=True, default='')

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', default=None, null=True, blank=True)
    tier = models.CharField(max_length=10, choices=COLLECTIBLE_TIERS, default='TIER_5')
    
    owner = models.ForeignKey(Player, default=None, null=True, blank=True, on_delete=models.SET_NULL)
    @property
    def is_bought(self):
        return self.owner is not None
    
    @property
    def bids(self):
        if not self.is_bought:
            return []
        else:
            purchase_requests = PurchaseRequest.objects.filter(nft_token=self.token)
            return purchase_requests.filter(is_accepted=False)
    
    @property
    def max_bid(self):
        max_bid = self.bids[0]
        for bid in self.bids[1:]:
            if bid.amount > max_bid.amount:
                max_bid = bid
        return max_bid

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        print('Save function...')
        if not self.token or self.token == "": self.token = str(uuid.uuid4()).replace('-', '')[:12]
        super(NFTCollectible, self).save(*args, **kwargs)

class LootboxTier(models.Model):
    title = models.CharField(max_length=100)
    included_tiers = MultiSelectField(choices=COLLECTIBLE_TIERS, max_choices = 5, max_length=100)
    coins_price = models.IntegerField(default=0.0)

    def __str__(self) -> str:
        return f'{self.included_tiers} - {self.coins_price}'

    def random_collectibles(self):
        collectible_sets = []

        for tier in self.included_tiers:
            print(tier)
            query = NFTCollectible.objects.filter(tier=tier)
            query = [collectible for collectible in query if not collectible.is_bought]

            tier_num = int(tier.split('_')[1])
            collectible_sets.append({'tier': tier_num, 'collectibles': query})
        
        collectible_sets.sort(key=lambda x: x['tier'], reverse=False)
        num_selected_tiers = len(collectible_sets)

        selected_collectibles = []

        # Starts from the most valuable tier and goes to the lowest valuable tier
        for i, tier_set in enumerate(collectible_sets):
            tier_num = tier_set['tier']
            collectibles = tier_set['collectibles']
            if len(collectibles) == 0: continue
            selected_num = (num_selected_tiers - i) * 2
            if selected_num > len(collectibles): selected_num = len(collectibles)
            selected_collectibles += random.sample(collectibles, selected_num)
        return selected_collectibles

