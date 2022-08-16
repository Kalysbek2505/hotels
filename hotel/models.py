from tkinter import CASCADE
from django.db import models
from account.models import User

STATUS = ((0, 'Не забронировано'), (1, 'Забронировано'))

class Room(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    adress = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, related_name='rooms', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='rooms', null=True, blank=True)
    status = models.IntegerField(choices=STATUS)
    def __str__(self):
        return f"{self.user.username} => {self.title}"
    @property
    def average_rating(self):
        ratings = [rating.value for rating in self.ratings.all()]
        if ratings:
            return sum(ratings) / len(ratings)
        return 0



class Rating(models.Model):
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='ratings', on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])



class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='comments', on_delete=models.CASCADE)    
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment{self.user.username} -> {self.room.title} [{self.created_at}]"


class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='likes', on_delete=models.CASCADE)
    def __str__(self):
        return f"Like{self.user.username} -> {self.room.title}"


class Booking(models.Model):
    user = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='bookings', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
<<<<<<< HEAD
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()
=======
    statususer = models.IntegerField(Room, choices=STATUS, default=1)


    
>>>>>>> e43e764881aebe0932e35f9adab9a8dd8ab7dc12


class Favorite(models.Model):
    user = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='favorites', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} -> {self.room.title}"


