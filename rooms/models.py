from django.db import models

from django_countries.fields import CountryField


from core import models as core_models
# foreign key 
from users import models as user_models

class AbstractItem(core_models.TimeStampedModel):
    """ Abstract Item """
    name = models.CharField(max_length=80)

    class Meta:
        abstract = True
        
    def __str__(self):
        return self.name

class RoomType(AbstractItem):
    #상속
    """ RoomType Model Definition"""
    class Meta:
        verbose_name = "Room Type"

class Amenity(AbstractItem):
    """ Amenity Model Definition"""
    class Meta:
        verbose_name_plural  = "Amenities"

class Facility(AbstractItem):
    """ Facility Model Definition """
    class Meta:
        verbose_name_plural  = "Facilities"

class HouseRule(AbstractItem):
    """ HouseRule Model Definition """
    class Meta:
        verbose_name = "House Rule"



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
    host = models.ForeignKey(user_models.User, related_name="rooms", on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, related_name="rooms", on_delete=models.SET_NULL, null=True)
    #on_delete=models.SET_NULL : 룸타입 삭제하더라도 룸이 삭제되지 않도록 설정
    amenities = models.ManyToManyField(Amenity, related_name="rooms", blank=True)
    facilities = models.ManyToManyField(Facility, related_name="rooms", blank=True)
    house_rules = models.ManyToManyField(HouseRule, related_name="rooms", blank=True)

    def __str__(self):
        return self.name
        #name에 self 스트링 지정

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating_average()
        return all_ratings / len(all_reviews)

class Photo(core_models.TimeStampedModel):
    """ Photo Model Definition """
    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey(Room, related_name="photos", on_delete=models.CASCADE)
    #Room정의가 되어 있지 않음. 파이썬은 파일을 상하수직형으로 읽기 때문임. 
    #그래서 class Photo에서 Room 클래스를 호출하려면, class Room 밑에 두어야 함
    def __str__(self):
        return self.caption

