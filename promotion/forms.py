from django import forms
from . models import PromoteNftPromo, BlockchainPromo, MarketplacePromo

class PromoteFormPromo(forms.ModelForm):
    class Meta:
        model = PromoteNftPromo
        fields = ["image", "title", "blockchain", "marketplace", "link", "twiter", "website", "discord"]

        widget = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "blockchain": forms.Select(attrs={"class": "form-control"}),
            "marketplace": forms.Select(attrs={"class": "form-control"}),
            "link": forms.Textarea(attrs={"class": "form-control"}),
            "twiter": forms.Textarea(attrs={"class": "form-control"}),
            "website": forms.Textarea(attrs={"class": "form-control"}),
            "discord": forms.Textarea(attrs={"class": "form-control"})
        }

class BlochchainFormPromo(forms.ModelForm):
    class Meta:
        model = BlockchainPromo
        fields = ["blockp"]

        widget = {
            "blockp": forms.TextInput(attrs={"class": "from-control"})
        }

class MarketplaceFormPromo(forms.ModelForm):
    class Meta:
        model = MarketplacePromo
        fields = ["marketp"]

        widget = {
            "marketp": forms.TextInput(attrs={"class": "form-control"})
        }