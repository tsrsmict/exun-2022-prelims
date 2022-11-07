from django.db import models
from django.contrib.auth.models import User

import uuid

# Create your models here.
class NFTCollectible(models.Model):
    token = models.CharField(max_length=100, editable=False, unique=True)

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default=None, null=True, blank=True)
    price = models.FloatField()
    
    user = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.SET_NULL)
    @property
    def is_bought(self):
        return self.user is not None

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        print('Save function...')
        if not self.token or self.token == "": self.token = str(uuid.uuid4()).replace('-', '')[:12]
        super(NFTCollectible, self).save(*args, **kwargs)

class PurchaseRequest(models.Model):
    nft = models.ForeignKey(NFTCollectible, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.SET_NULL)

    datetime = models.DateTimeField(auto_now_add=True)

    @property
    def receiver(self):
        return self.nft.user
    
    def __str__(self):
        return f"{self.sender} wants to buy {self.nft} from {self.receiver}"
