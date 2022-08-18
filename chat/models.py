from django.db import models
from AccountApp.models import User

class Room(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1', db_column='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2', db_column='user2')

# Create your models here.
class Message(models.Model):
    message = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', db_column='user', null=True, max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages', db_column='room', null=True)
    sort = models.CharField(max_length=30, null=True)

class Thema(models.Model):
    sort = models.CharField(max_length=10, null=True)
    number = models.PositiveIntegerField()
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='thema1', db_column='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='thema2', db_column='user2')

class ThemaMessage(Message):
    thema_sort = models.CharField(max_length=10, null=True)
    number = models.PositiveIntegerField()
    confirmed = models.BooleanField(default=False)




