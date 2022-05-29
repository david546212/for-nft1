from django.shortcuts import render, redirect

from . models import BlockchainPromo, MarketplacePromo, PromoteNftPromo, Promotion
from . forms import PromoteFormPromo, BlochchainFormPromo, MarketplaceFormPromo

# Create your views here.

def index(request):
    x = request.GET.get("x") if request.GET.get("x") != None else ""
    xx = request.GET.get("xx") if request.GET.get("xx") != None else ""

    postspromo = PromoteNftPromo.objects.filter(blockchain__blockp__icontains=x, marketplace__marketp__icontains=xx)
    blockchainpromo = BlockchainPromo.objects.all()
    marketplacepromo = MarketplacePromo.objects.all()
    promo = Promotion.objects.all()

    context = {
        "postspromo": postspromo, "blockchainpromo": blockchainpromo, "marketplacepromo": marketplacepromo, "promo": promo
    }

    return render(request, "second_base.html", context)

def promote(request):
    form = PromoteFormPromo()
    if request.method == "POST":
        form = PromoteFormPromo(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("promote")
    context = {
        "form1": form
    }
    return render(request, "promotion_form.html", context)

def detail_promote(request, title, pk):
    promote_detail = PromoteNftPromo.objects.get(title=title, pk=pk)
    context = {
        "promote_detail": promote_detail
    }
    return render(request, "detail_promotion.html", context)

def blockchain_new(request):
    form = BlochchainFormPromo()
    if request.method == "POST":
        form = BlochchainFormPromo(request.POST)
        if form.is_valid():
            form.save()
            return redirect("promote-new")
    context = {
        "form1": form
    }
    return render(request, "form_blockchain.html", context)

def marketplace_new(request):
    form = MarketplaceFormPromo()
    if request.method == "POST":
        form = MarketplaceFormPromo(request.POST)
        if form.is_valid():
            form.save()
            return redirect("promote-new")
    context = {
        "form1": form
    }
    return render(request, "form_marketplace.html", context)