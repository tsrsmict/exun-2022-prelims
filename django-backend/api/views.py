from django.contrib.auth.models import User

from rest_framework import viewsets

from .serializers import UserSerializer, NFTCollectibleSerializer
from .models import NFTCollectible

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class NFTCollectibleViewSet(viewsets.ModelViewSet):
    queryset = NFTCollectible.objects.all()
    serializer_class = NFTCollectibleSerializer