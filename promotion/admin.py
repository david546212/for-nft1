from django.contrib import admin
from . models import BlockchainPromo, MarketplacePromo, PromoteNftPromo

# Register your models here.

admin.site.register(BlockchainPromo)
admin.site.register(MarketplacePromo)
admin.site.register(PromoteNftPromo)