from django.contrib import admin
from . import models as models
# Register your models here.
@admin.register(models.NFTCollectible)
class NFTCollectibleAdmin(admin.ModelAdmin):
    pass

@admin.register(models.PurchaseRequest)
class PurchaseRequestAdmin(admin.ModelAdmin):
    pass