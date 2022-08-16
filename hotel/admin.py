from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('created_at',)

admin.site.register(Room)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Rating)
<<<<<<< HEAD
admin.site.register(Booking, PostAdmin)
=======
admin.site.register(Favorite)
admin.site.register(Booking)
>>>>>>> d505fc8e30ef3d4d46bdb23fd23c37b9272451c8
