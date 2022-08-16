from django.contrib import admin
from .models import *

admin.site.register(Room)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Rating)
admin.site.register(Favorite)
admin.site.register(Booking)