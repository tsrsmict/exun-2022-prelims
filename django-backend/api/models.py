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
    nft = models.ForeignKey('NFTCollectible', default=None, null=True, blank=True, on_delete=models.CASCADE)
    sender = models.ForeignKey(Player, default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='sender')
    receiver = models.ForeignKey(Player, default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name='receiver')
    datetime_sent = models.DateTimeField(auto_now_add=True)

    amount_spacebucks = models.FloatField(default=0.0)
    
    is_accepted = models.BooleanField(default=False)
    datetime_accepted = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.sender} wants to buy {self.nft} from {self.receiver} for {self.amount_spacebucks} spacebucks"

class NFTCollectible(models.Model):
    token = models.CharField(max_length=100, editable=False, unique=True, default='')

    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images', default=None, null=True, blank=True)
    tier = models.CharField(max_length=10, choices=COLLECTIBLE_TIERS, default='TIER_5')
    
    owner = models.ForeignKey(Player, default=None, null=True, blank=True, on_delete=models.SET_NULL)
    @property
    def is_unmined(self):
        return self.owner is None
    
    @property
    def bids(self):
        if self.is_unmined:
            return []
        else:
            purchase_requests = PurchaseRequest.objects.filter(nft__token=self.token)
            return purchase_requests.filter(is_accepted=False)
    
    @property
    def max_bid(self):
        max_bid = self.bids[0]
        for bid in self.bids[1:]:
            if bid.amount_spacebucks > max_bid.amount_spacebucks:
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
            query = [collectible for collectible in query if collectible.is_unmined]
            if len(query) == 0:
                continue

            tier_num = int(tier.split('_')[1])
            collectible_sets.append({'tier': tier_num, 'collectibles': query})
        
        collectible_sets.sort(key=lambda x: x['tier'], reverse=False)
        print('Got matching sets', collectible_sets)
        
        # For now, just select one of each tier
        selected_collectibles = []
        for collectible_set in collectible_sets:

            selected_collectibles.append(random.choice(collectible_set['collectibles']))
        return selected_collectibles

