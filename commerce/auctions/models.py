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
    #Um ou mais usuário tem várias listagens
    

class Bids():
    pass
    #ID (PK)
    #Bid Value
    #One bid replace the last, if the actual is greater (Comparison)
    #UserName - FK
    #Datatime
    #Um ou mais usuários pode ter mais de uma Bid

class Comments():
    pass
    #ID (PK)
    #Comment
    #UserName - FK
    #Um ou mais usuários pode ter mais de um Comment
