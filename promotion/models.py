from django.db import models

# Create your models here.
default_id = 1

class BlockchainPromo(models.Model):
    blockp = models.CharField(max_length=10000)

    def __str__(self):
        return self.blockp

class MarketplacePromo(models.Model):
    marketp = models.CharField(max_length=10000)

    def __str__(self):
        return self.marketp

class PromoteNftPromo(models.Model):
    image = models.ImageField(null=False)
    title = models.CharField(max_length=60)
    blockchain = models.ForeignKey(BlockchainPromo, on_delete=models.SET_NULL, null=True, default=default_id)
    marketplace = models.ForeignKey(MarketplacePromo, on_delete=models.SET_NULL, null=True, default=default_id)
    link = models.CharField(max_length=10000)
    created = models.DateTimeField(auto_now_add=True)
    twiter = models.CharField(max_length=10000, blank=True)
    website = models.CharField(max_length=10000, blank=True)
    discord = models.CharField(max_length=10000, blank=True)
    
    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
