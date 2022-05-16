from django.contrib import admin

# Register your models here.

from .models import NewEvent
from .models import Blockchain
from .models import Marketplace

admin.site.register(NewEvent)
admin.site.register(Blockchain)
admin.site.register(Marketplace)