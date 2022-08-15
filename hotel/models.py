from django.db import models
from account.models import User

class Room(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    user = models.ForeignKey(User, related_name='rooms', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='rooms', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} => {self.title}"
    @property
    def average_rating(self):
        ratings = [rating.value for rating in self.ratings.all()]
        if ratings:
            return sum(ratings) / len(ratings)
        return 0

    @property
    def average_rating(self):
        ratings = [rating.value for rating in self.ratings.all()]
        if ratings:
            return sum(ratings) / len(ratings)
        return 0

class Rating(models.Model):
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    product = models.ForeignKey(Room, related_name='ratings', on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])

class Comment(models.Model):
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Room, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment{self.user.username} -> {self.post.title} [{self.created_at}]"


class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Room, related_name='likes', on_delete=models.CASCADE)
    def __str__(self):
        return f"Like{self.user.username} -> {self.post.title}"

