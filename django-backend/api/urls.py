
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

urlpatterns = [
    path('', include(user_router.urls)),
    path('', include(nft_router.urls)),
    path('', include(purchase_router.urls)),
    path('', include(player_router.urls)),

    path('open-lootbox/', views.OpenLootboxView.as_view(), name='open-lootbox'),
    path('token-auth/', views.CustomAuthToken.as_view(), name='auth_token'),
]