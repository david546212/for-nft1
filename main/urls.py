from . import views
from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", views.index, name="index"),
    path("new-post/", views.newevent, name="newpost"),
    path("detail-drop/<title>/<str:pk>/", views.detail_drop, name="detail_drop"),
    path("marketplace-new/", views.new_marketplace, name="new-marketplace"),
    path("blockchain-new/", views.new_blockchain, name="new-blockchain"),
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("img/favicon.ico"))),
    path("privacy-policy/", views.privacy, name="privacy"),
    path("terms-of-use/", views.terms, name="terms")
]