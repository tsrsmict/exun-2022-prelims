from django.db import models
from django.contrib.auth.models import User

import uuid

# Create your models here.
class NFTCollectible(models.Model):
    token = models.CharField(max_length=100)

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    price = models.FloatField()
    
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL)
    @property
    def is_bought(self):
        return self.user is not None

    def __str__(self):
        return self.name
    
    def __save__(self, *args, **kwargs):
        if not self.token: self.token = str(uuid.uuid4())[:12]
        super(NFTCollectible, self).save(*args, **kwargs)