<<<<<<< HEAD
from django.contrib import admin
from . import models

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    pass
=======
from django.contrib import admin
from . import models


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass
>>>>>>> fa6c254c8ad9c40b6332389b78c08fb063522724
