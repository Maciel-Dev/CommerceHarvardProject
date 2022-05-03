from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class AuctionListing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1024)
    startBid = models.IntegerField(max_length=99999)
    imageUrl = models.URLField(max_length=2048, blank=True, null=True)
    
    #Um ou mais usuário tem várias listagens
    

class Bids(models.Model):
    bidValue = models.DecimalField(max_digits=6, decimal_places=2)
    userName = models.ForeignKey(User)
    dateTime = models.DateTimeField(auto_now_add=True)

    #One bid replace the last, if the actual is greater (Comparison)

    #Um ou mais usuários pode ter mais de uma Bid

class Comments():
    pass
    #ID (PK)
    comment = models.TextField(max_length=1024)
    userName = models.ForeignKey(User)
    #Possibilidade de colocar datetime
    #Um ou mais usuários pode ter mais de um Comment
