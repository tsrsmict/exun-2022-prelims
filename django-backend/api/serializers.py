from django.contrib.auth.models import User
from rest_framework import serializers

from . import models as models

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class NFTCollectibleSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    class Meta:
        model = models.NFTCollectible
        fields = ['token', 'name', 'description', 'image', 'price', 'user_id', 'is_bought']

class PurchaseRequest(serializers.ModelSerializer):
    nft_token = serializers.CharField(source='nft.token', read_only=True)
    sender_id = serializers.ReadOnlyField(source='sender.id')
    receiver_id = serializers.ReadOnlyField(source='receiver.id')

    class Meta:
        model = models.PurchaseRequest
        fields = ['nft_token', 'sender_id', 'receiver_id', 'datetime_sent', 'datetime_accepted', 'has_been_accepted']