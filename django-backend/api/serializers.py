from django.contrib.auth.models import User
from rest_framework import serializers

from .models import NFTCollectible

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class NFTCollectibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFTCollectible
        fields = ['token', 'name', 'description', 'image', 'price', 'user', 'is_bought']