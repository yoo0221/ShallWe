from django.db import models
from AccountApp.models import User

# Create your models here.
class Message(models.Model):
    message = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)

class Room(models.Model):
    user1 = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user1', db_column='user1')
    user2 = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user2', db_column='user2')