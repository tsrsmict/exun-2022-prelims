from functools import reduce
import datetime

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

class PurchaseRequestViewSet(viewsets.ReadOnlyModelViewSet):
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
        if collectible_tier.coins_price > player.coins:
            return HttpResponse('Insufficient funds', status=400)

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

        player.coins -= collectible_tier.coins_price
        player.save()

        return HttpResponse(renderer.render(res), content_type='application/json', status=200)

class SubmitPurchaseRequestView(APIView):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]  

    def post(self, request):
        try:
            player = models.Player.objects.get(account__id=request.user.id)
        except Exception as e:
            print(e)
            return HttpResponse('Invalid player ID', status=400)

        collectible_id = request.POST.get('collectible', None)
        if not collectible_id:
            return HttpResponse('No collectible specified', status=400)
        
        try:
            collectible = models.NFTCollectible.objects.get(id=collectible_id)
        except Exception as e:
            print(e)
            return HttpResponse('Invalid collectible ID', status=400)
        
        if collectible.is_unmined:
            return HttpResponse('Cannot buy an unmined collectible', status=400)
        
        amount = (request.POST.get('amount', None))
        if not amount:
            return HttpResponse('No amount specified', status=400)     
        amount = int(amount)

        if amount < 1:
            return HttpResponse('Invalid amount', status=400)

        if amount >= player.spacebucks:
            return HttpResponse('Insufficient funds', status=400)       
        
        current_owner = collectible.owner
        print(f'Current owner: {current_owner}')
        if current_owner == player:
            return HttpResponse('You already own this collectible', status=400)
        
        # Check if the player already has a purchase request for this collectible
        if models.PurchaseRequest.objects.filter(nft=collectible, sender=player).exists():
            return HttpResponse('You already have a purchase request for this collectible', status=400)
        

        # Create a pruchase request
        purchase_request = models.PurchaseRequest.objects.create(nft=collectible, sender=player, receiver=current_owner, amount_spacebucks=amount, datetime_sent=datetime.datetime.now())
        purchase_request.save()
        
        renderer = JSONRenderer()
        res = {
            "success": True,
            "purchase_request": custom_serializers.PurchaseRequestSerializer(purchase_request).data,
        }

        return HttpResponse(renderer.render(res), content_type='application/json', status=200)

class AcceptPurchaseRequestView(APIView):
    def post(self, request):
        try:
            receiver = models.Player.objects.get(account__id=request.user.id)
        except Exception as e:
            print(e)
            return HttpResponse('Invalid player ID', status=400)
        
        purchase_request_id = request.POST.get('purchase_request', None)
        if not purchase_request_id:
            return HttpResponse('No purchase request specified', status=400)
        
        try:
            purchase_request = models.PurchaseRequest.objects.get(id=purchase_request_id)
        except Exception as e:
            print(e)
            return HttpResponse('Invalid purchase request ID', status=400)

        if purchase_request.is_accepted:
            return HttpResponse('Purchase request already accepted', status=400)

        if purchase_request.receiver != receiver:
            return HttpResponse('You do not own this collectible', status=400)
        
        # Accept the purchase request
        purchase_request.is_accepted = True
        purchase_request.datetime_accepted = datetime.datetime.now()

        sender = purchase_request.sender
        
        # Transfer the collectible to the buyer
        purchase_request.nft.owner = purchase_request.sender
        purchase_request.save()
        purchase_request.nft.save()
        
        # Add the price of the collectible to the seller's account
        receiver.spacebucks += purchase_request.amount_spacebucks
        receiver.save()

        # Subtract the price of the collectible from the buyer's account
        sender.spacebucks -= purchase_request.amount_spacebucks
        sender.save()

        # Change the receiver of all other purchase requests for this collectible to the buyer
        for pr in models.PurchaseRequest.objects.filter(nft=purchase_request.nft, is_accepted=False):
            pr.receiver = sender
            pr.save()

        renderer = JSONRenderer()
        res = {
            "success": True,
            "purchase_request": custom_serializers.PurchaseRequestSerializer(purchase_request).data,
        }

        return HttpResponse(renderer.render(res), content_type='application/json', status=200)

class PlayerViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = models.Player.objects.all()
    serializer_class = custom_serializers.PlayerSerializer