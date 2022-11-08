from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework import serializers

from . import models as models

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['url', 'username', 'password']

class PurchaseRequestSerializer(serializers.ModelSerializer):
    for_token = serializers.CharField(source='nft.token')
    sender = serializers.IntegerField(source='sender.id')
    receiver = serializers.ReadOnlyField(source='receiver.id')
    amount_spacebucks = serializers.IntegerField()

    datetime_accepted = serializers.DateTimeField(read_only=True)
    is_accepted = serializers.BooleanField(read_only=True)

    class Meta:
        model = models.PurchaseRequest
        fields = ['id', 'for_token', 'sender', 'receiver', 'amount_spacebucks', 'datetime_sent', 'is_accepted', 'datetime_accepted']

class NFTCollectibleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    bids = serializers.ListField(child=PurchaseRequestSerializer(), read_only=True)
    class Meta:
        model = models.NFTCollectible
        fields = ['token', 'name', 'description', 'image', 'tier', 'owner', 'is_unmined', 'bids']

class LootboxTierSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LootboxTier
        fields = ['id', 'title', 'included_tiers', 'coins_price']

class PlayerSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='user.id')
    account = serializers.IntegerField(source='account.id', read_only=True)
    spacebucks = serializers.FloatField(read_only=True)
    coins = serializers.IntegerField(read_only=True)
    collectibles = NFTCollectibleSerializer(many=True, read_only=True)
    class Meta:
        model = models.Player
        fields = ['id', 'account', 'username', 'profile_image', 'spacebucks', 'coins', 'collectibles']
    
    def create(self, validated_data):
        print(validated_data)
        user = User.objects.get(id=validated_data['account'])
        player = models.Player.objects.create(account=user, profile_image=validated_data['profile_image'])
        return player