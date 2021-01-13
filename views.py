from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms
from datetime import datetime

from .models import User, Listing, Comment, Bid, Watchlistitem
from .helper import getWatchlistNum, getComments

def index(request):
    watchlistnum = getWatchlistNum(request.user.username)

    return render(request, "auctions/index.html", {
        "listings": Listing.objects.order_by('datetime').reverse(),
        "watchlistnum": watchlistnum
    })

def closedlistings(request):
    watchlistnum = getWatchlistNum(request.user.username)

    return render(request, "auctions/closedlistings.html", {
        "listings": Listing.objects.order_by('datetime').reverse(),
        "watchlistnum": watchlistnum
    })

def viewlisting(request, listing_id):
    listing = Listing.objects.get(id=listing_id)

    watchlist = True
    try:
        Watchlistitem.objects.get(buyer = request.user.username).buyer == request.user.username
    except:
        watchlist = False

    return render(request, "auctions/listing.html", {
        "listing": listing,
        "comments": getComments(listing_id), 
        "watchlist": watchlist,
        "watchlistnum": getWatchlistNum(request.user.username)
    })

@login_required
def createlisting(request):
    if request.method == "POST":
        
        seller = request.user.username
        name = request.POST["name"]
        startingbid = request.POST['startingbid']
        description = request.POST['description']
        image = request.POST['image']
        name = request.POST['name']
        category = request.POST["category"]

        listing = Listing.objects.create(seller = seller, name = name, startingbid = startingbid, description = description, image = image, category = category, highestbid = int(startingbid) - 1)

        listing.save()

        return render(request, "auctions/listing.html", {
            "listing": listing,
            "watchlistnum": getWatchlistNum(request.user.username),
            "comments": getComments(listing.id), 
        })

    else:
        return render(request, "auctions/createlisting.html", {
            "listings": Listing.objects.all(),
            "watchlistnum": getWatchlistNum(request.user.username)
        })

@login_required
def watchlist(request):

    useritems = Watchlistitem.objects.filter(buyer = request.user.username)
    listings = []

    for item in useritems:
        listings.append(Listing.objects.get(id = item.listingid))

    if len(listings) == 0:
        return render(request, "auctions/watchlist.html", {
            "listings": listings,
            "watchlistnum": getWatchlistNum(request.user.username),
            "message": "There are no items in your watchlist."
        })
    else:
        return render(request, "auctions/watchlist.html", {
            "listings": listings,
            "watchlistnum": getWatchlistNum(request.user.username),
        })

def category(request, category):

    listings = Listing.objects.filter(category = category)

    if len(listings) == 0:
        return render(request, "auctions/category.html", {
            "category": category,
            "listings": listings,
            "watchlistnum": getWatchlistNum(request.user.username),
            "message": "There are no items in this category."
        })
    else:
        return render(request, "auctions/category.html", {
            "category": category,
            "listings": listings,
            "watchlistnum": getWatchlistNum(request.user.username),
        })

@login_required
def addwatchlist(request, listing_id):

    listing = Listing.objects.get(id=listing_id)

    for item in Watchlistitem.objects.all():
        if item.listingid == listing_id and request.user.username == item.buyer:

            item.delete()

            return render(request, "auctions/listing.html", {
                "listing": listing,  
                "watchlist": False,
                "comments": getComments(listing_id), 
                "watchlistnum": getWatchlistNum(request.user.username)
            })
    
    new = Watchlistitem.objects.create(buyer = request.user.username, listingid = listing_id)
    new.save()

    return render(request, "auctions/listing.html", {
        "listing": listing,
        "watchlist": True,
        "comments": getComments(listing_id), 
        "watchlistnum": getWatchlistNum(request.user.username)
    })

@login_required
def makebid(request, listing_id):
    listing = Listing.objects.get(id = listing_id)
    price = int(request.POST["price"])

    if (price > listing.highestbid):

        buyer = request.user.username
        name = listing.name
        Bid.objects.create(buyer = buyer, name = name, price = price)

        listing.highestbid = price
        listing.save()

        return render(request, "auctions/listing.html", {
            "listing": listing,
            "comments": getComments(listing_id), 
            "watchlistnum": getWatchlistNum(request.user.username)
        })
    
    else:

        return render(request, "auctions/listing.html", {
            "listing": listing,
            "message": "Your bid must be greater than the current bid",
            "comments": getComments(listing_id), 
            "watchlistnum": getWatchlistNum(request.user.username)
        })

@login_required
def addcomment(request, listing_id):
    buyer = request.user.username

    listing = Listing.objects.get(id=listing_id)
    title = listing.name
    message = request.POST["comment"]

    new = Comment.objects.create(buyer = buyer, title = title, message = message, listingid = listing_id)
    new.save()

    return render(request, "auctions/listing.html", {
        "listing": listing, 
        "comments": getComments(listing_id), 
        "watchlistnum": getWatchlistNum(request.user.username)
    })

@login_required
def closelisting(request, listing_id):

    listing = Listing.objects.get(id = listing_id)
    listing.isactive = False
    listing.winner = Bid.objects.get(price = listing.highestbid).buyer
    listing.save()

    return viewlisting(request, listing_id)

#SuperUser: BJ is username, password is known
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

    return render(request, "auctions/register.html")
