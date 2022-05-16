from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="promote"),
    path("new-promotion/", views.promote, name="promote-new"),
    path("detail-promotion/<title>/<str:pk>/", views.detail_promote, name="detail_promotion"),
    path("new-marketplace/", views.marketplace_new, name="marketplace"),
    path("new-blochchain/", views.blockchain_new, name="new_blockchain")
]