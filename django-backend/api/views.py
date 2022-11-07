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
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from . import serializers as custom_serializers
from . import models as models


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = custom_serializers.UserSerializer

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
        })

class NFTCollectibleViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.NFTCollectible.objects.all()
    serializer_class = custom_serializers.NFTCollectibleSerializer

class PurchaseRequestViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.PurchaseRequest.objects.all()
    serializer_class = custom_serializers.PurchaseRequestSerializer

class LootboxTierViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.LootboxTier.objects.all()
    serializer_class = custom_serializers.LootboxTierSerializer  

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
        player.save()

        # Get the lootbox tier's NFTs
        nfts = collectible_tier.random_collectibles()
        for nft in nfts:
            nft.owner = player
            nft.save()
        nft_data = custom_serializers.NFTCollectibleSerializer(nfts, many=True).data
        
        renderer = JSONRenderer()
        account_data = (custom_serializers.PlayerSerializer(player).data)

        res = {
            "success": len(nfts) > 0,
            "acquired_collectibles": nft_data,
            "account": account_data,
        }

        return HttpResponse(renderer.render(res), content_type='application/json', status=200)

class PlayerViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = models.Player.objects.all()
    serializer_class = custom_serializers.PlayerSerializer

""""
coins for lootboxes
spacebucks for marketplace
"""