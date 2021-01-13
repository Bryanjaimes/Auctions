from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):
    pass
  
class Bid(models.Model):
    buyer = models.CharField(max_length = 64, default = "NULL")
    name = models.CharField(default = "NULL", max_length = 64)
    price = models.IntegerField(default = 0)

    def __str__(self):
        return f"{self.buyer} has placed a bid of {self.price} on {self.name}"

class Comment(models.Model):
    buyer = models.CharField(max_length = 64, default = "NULL")
    title = models.CharField(default = "NULL", max_length = 1024)
    message = models.CharField(default = "NULL", max_length = 1024)
    datetime = models.DateTimeField(default = datetime.now)
    listingid = models.IntegerField(default = 0)
    
    def __str__(self):
        return f"{self.buyer} wrote {self.message} on {self.title} on {self.datetime}"

class Listing(models.Model):
    seller = models.CharField(max_length = 64, default = "NULL")
    name = models.CharField(default = "NULL", max_length = 64)
    startingbid = models.IntegerField(default = 0)
    image = models.CharField(default = "None", blank = True, null = True, max_length = 1024)
    datetime = models.DateTimeField(default = datetime.now)
    description = models.CharField(default = "NULL", max_length = 1024)
    bid = models.ManyToManyField(Bid, blank = True, related_name = "bid")
    comment = models.ManyToManyField(Comment, blank = True, related_name = "comment")
    isactive = models.BooleanField(default = True)
    highestbid = models.IntegerField(default = 0)
    category = models.CharField(max_length = 64, default = "NULL")
    winner = models.CharField(max_length = 64, default = "NULL")

    def __str__(self):
        return f"{self.name} has a starting bid of ${self.startingbid}"

class Watchlistitem(models.Model):
    buyer = models.CharField(max_length = 64)
    listingid = models.IntegerField(default = 0)

    def __str__(self):
        return f"{self.buyer} has watchlist item with id number {self.listingid}"




