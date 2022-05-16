from django.shortcuts import render, redirect
from .models import NewEvent, Blockchain, Marketplace
from .forms import EventForm, BlochchainForm, MarketplaceForm


# Create your views here.


def index(request):
    qq = request.GET.get("qq") if request.GET.get("qq") != None else ""
    qqq = request.GET.get("qqq") if request.GET.get("qqq") != None else ""

    posts = NewEvent.objects.filter(blockchain__block__icontains=qq, marketplace__market__icontains=qqq)
    blockchain = Blockchain.objects.all()
    marketplace = Marketplace.objects.all()

    context = {
        "posts": posts, "blockchain": blockchain, "marketplace": marketplace
    }

    return render(request, "index.html", context)

def newevent(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {
        "form": form
    }
    return render(request, "event_form.html", context)

def detail_drop(request, title, pk):
    drop = NewEvent.objects.get(title=title, pk=pk)
    context = {
        "release": drop
    }
    return render(request, "detail_drop.html", context)

def new_blockchain(request):
    form = BlochchainForm()
    if request.method == "POST":
        form = BlochchainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("newpost")
    context = {
        "form": form
    }
    return render(request, "blockchain_form.html", context)

def new_marketplace(request):
    form = MarketplaceForm()
    if request.method == "POST":
        form = MarketplaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("newpost")
    context = {
        "form": form
    }
    return render(request, "marketplace_form.html", context)

def privacy(request):
    return render(request, "privacy_policy.html")

def terms(request):
    return render(request, "terms_of_use.html")