from django.contrib.auth.models import User

from rest_framework import viewsets

from . import serializers as custom_serializers
from . import models as models

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = custom_serializers.UserSerializer

class NFTCollectibleViewSet(viewsets.ModelViewSet):
    queryset = models.NFTCollectible.objects.all()
    serializer_class = custom_serializers.NFTCollectibleSerializer

class PurchaseRequestViewSet(viewsets.ModelViewSet):
    queryset = models.PurchaseRequest.objects.all()
    serializer_class = custom_serializers.PurchaseRequest