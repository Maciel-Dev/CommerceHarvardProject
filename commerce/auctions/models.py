from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class AuctionListing():
    pass
    #ID (Pk)
    #Title
    #Description
    #Start Bid
    #OPtional - Image URl
    

class Bids():
    pass
    #ID (PK)
    #Bid Value
    #One bid replace the last, if the actual is greater (Comparison)
    #UserName - FK
    #Datatime

class Comments():
    pass
    #ID (PK)
    #Comment
    #UserName - FK
