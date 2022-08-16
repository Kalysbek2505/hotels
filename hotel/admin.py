from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('created_at',)

admin.site.register(Room)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Rating)
admin.site.register(Favorite)
admin.site.register(Booking)
admin.site.register(Chat)

