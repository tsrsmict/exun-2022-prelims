from django.contrib import admin
from .models import NFTCollectible
# Register your models here.
@admin.register(NFTCollectible)
class NFTCollectibleAdmin(admin.ModelAdmin):
    pass