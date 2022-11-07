
from django.urls import path, include

from rest_framework import routers

from . import views as views

# Routers provide an easy way of automatically determining the URL conf.
user_router = routers.DefaultRouter()
user_router.register(r'users', views.UserViewSet)

nft_router = routers.DefaultRouter()
nft_router.register(r'nft-collectibles', views.NFTCollectibleViewSet)

purchase_router = routers.DefaultRouter()
purchase_router.register(r'purchase-requests', views.PurchaseRequestViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(user_router.urls)),
    path('', include(nft_router.urls)),
    path('', include(purchase_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]