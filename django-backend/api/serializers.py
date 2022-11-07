from django.contrib.auth.models import User
from rest_framework import serializers

from . import models as models

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class PurchaseRequestSerializer(serializers.ModelSerializer):
    nft_token = serializers.CharField(source='nft.token', read_only=True)
    sender_id = serializers.ReadOnlyField(source='sender.id')
    receiver_id = serializers.ReadOnlyField(source='receiver.id')
    datetime_accepted = serializers.DateTimeField(read_only=True)
    is_accepted = serializers.BooleanField(read_only=True)

    class Meta:
        model = models.PurchaseRequest
        fields = ['nft_token', 'sender_id', 'receiver_id', 'datetime_sent', 'is_accepted', 'datetime_accepted']

class NFTCollectibleSerializer(serializers.ModelSerializer):
    owner_id = serializers.ReadOnlyField(source='owner.id')
    bids = serializers.ListField(child=PurchaseRequestSerializer(), read_only=True)
    class Meta:
        model = models.NFTCollectible
        fields = ['token', 'name', 'description', 'image', 'tier', 'owner_id', 'bids']

class LootboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LootboxTier
        fields = ['included_tiers', 'price']

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Player
        fields = ['id', 'username', 'profile_image', 'spacebucks', 'game_coins', 'collectibles']