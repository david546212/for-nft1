from django import forms
from .models import NewEvent, Blockchain, Marketplace

class EventForm(forms.ModelForm):

    class Meta:
        model = NewEvent
        fields = ["image", "title", "release_date", "blockchain", "marketplace", "link", "twiter", "website", "discord"]

        widget = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "image"}),
            "release_date": forms.TextInput(attrs={"class": "form-control"}),
            "blockchain": forms.Select(attrs={"class": "form-control"}),
            "marketplace": forms.Select(attrs={"class": "form-control"}),
            "link": forms.TextInput(attrs={"class": "form-control"}),
            "twiter": forms.TextInput(attrs={"class": "form-control"}),
            "website": forms.TextInput(attrs={"class": "form-control"}),
            "discord": forms.TextInput(attrs={"class": "form-control"})
        }

class BlochchainForm(forms.ModelForm):

    class Meta:
        model = Blockchain
        fields = ["block"]

        widget = {
            "block": forms.TextInput(attrs={"class": "form-control"})
        }

class MarketplaceForm(forms.ModelForm):

    class Meta:
        model = Marketplace
        fields = ["market"]

        widget = {
            "market": forms.TextInput(attrs={"class": "form-control"})
        }