
from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken import views as authtoken_views

from . import views as views

# Routers provide an easy way of automatically determining the URL conf.
user_router = routers.DefaultRouter()
user_router.register(r'users', views.UserViewSet)

nft_router = routers.DefaultRouter()
nft_router.register(r'nft-collectibles', views.NFTCollectibleViewSet)

purchase_router = routers.DefaultRouter()
purchase_router.register(r'purchase-requests', views.PurchaseRequestViewSet)

player_router = routers.DefaultRouter()
player_router.register(r'players', views.PlayerViewSet)

lootbox_router = routers.DefaultRouter()
lootbox_router.register(r'lootbox-tiers', views.LootboxTierViewSet)

urlpatterns = [
    path('', include(user_router.urls)),
    path('', include(nft_router.urls)),
    path('', include(purchase_router.urls)),
    path('', include(player_router.urls)),
    path('', include(lootbox_router.urls)),

    path('open-lootbox/', views.OpenLootboxView.as_view(), name='open-lootbox'),
    path('make-purchase-request/', views.SubmitPurchaseRequestView.as_view(), name='purchase-request'),
    path('accept-purchase-request/', views.AcceptPurchaseRequestView.as_view(), name='accept-purchase-request'),

    path('get-token', views.CustomAuthToken.as_view(), name='auth_token'),
]