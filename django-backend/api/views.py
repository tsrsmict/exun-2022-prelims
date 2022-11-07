from functools import reduce
import operator

from django.contrib.auth.models import User
from django.db.models import Q

from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.http import HttpResponse

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
    serializer_class = custom_serializers.PurchaseRequestSerializer

class OpenLootboxView(APIView):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.POST
        lootbox_id = (data.get('lootbox', None))
        if not lootbox_id:
            return HttpResponse('No lootbox specified', status=400)
        else: lootbox_id = int(lootbox_id)

        # Get the lootbox tier from the database
        try:
            collectible_tier = models.LootboxTier.objects.get(id=lootbox_id)
        except Exception as e:
            print(e)
            return HttpResponse('Invalid lootbox ID', status=400)

        try:
            player = models.Player.objects.get(account__id=request.user.id)
        except Exception as e:
            print(e)
            return HttpResponse('Invalid player ID', status=400)
        
        # Subtract the value of the lootbox from the player's account
        player.coins -= collectible_tier.coins_price

        # Get the lootbox tier's NFTs
        nfts = collectible_tier.random_collectibles()
        for nft in nfts:
            nft.owner = player
            nft.save()        
        res_data = {"collectibles": [nft.token for nft in nfts]}
        res = JSONRenderer().render(res_data)

        return HttpResponse(res, content_type='application/json', status=200)

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = models.Player.objects.all()
    serializer_class = custom_serializers.PlayerSerializer

""""
coins for lootboxes
spacebucks for marketplace
"""