from .models import User, Listing, Comment, Bid, Watchlistitem

def getWatchlistNum(buyer):
    watchlistnum = len(Watchlistitem.objects.filter(buyer=buyer))
    return watchlistnum

def getComments(listing_id):
    comments = Comment.objects.filter(listingid=listing_id)
    return comments

