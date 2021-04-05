<<<<<<< HEAD
from django.db import models
from django_countries.fields import CountryField
from core import models as core_models

# foreign key 
from users import models as user_models 

class Room(core_models.TimeStampedModel):
    """ Room Model Definition """
    
    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
=======
from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as users_models


class Room(core_models.TimeStampedModel):
    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(users_models.User, on_delete=models.CASCADE)
    # host는 users 중에서도 나올 수 있기 때문에, users와 연결해줌
>>>>>>> fa6c254c8ad9c40b6332389b78c08fb063522724
