from django.db import models

# Create your models here.
default_id = 1

class Blockchain(models.Model):
    block = models.CharField(max_length=10000)

    def __str__(self):
        return self.block

class Marketplace(models.Model):
    market = models.CharField(max_length=10000)

    def __str__(self):
        return self.market

class NewEvent(models.Model):
    image = models.ImageField(null=False)
    title = models.CharField(max_length=60)
    release_date = models.CharField(max_length=50)
    blockchain = models.ForeignKey(Blockchain, on_delete=models.SET_NULL, null=True, default=default_id)
    marketplace = models.ForeignKey(Marketplace, on_delete=models.SET_NULL, null=True, default=default_id)
    link = models.CharField(max_length=10000)
    created = models.DateTimeField(auto_now_add=True)
    twiter = models.CharField(max_length=10000, blank=True)
    website = models.CharField(max_length=10000, blank=True)
    discord = models.CharField(max_length=10000, blank=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title

