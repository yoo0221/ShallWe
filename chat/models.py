from django.db import models
from AccountApp.models import User
# Create your models here.

# class Room(models.Model):
#     class Meta:
#         db_table = "room"

# class RoomJoin(models.Model):
#     user1_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="roomJoin", db_column="user1_id")
#     user2_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="roomJoin", db_column="user2_id")
#     room_id = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="roomJoin", db_column="room_id")
#     class Meta:
#         db_table="roomJoin"

# class Message(models.Model):
#     message = models.CharField(max_length=500)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="roomJoin", db_column="user_id")
#     room_id = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="roomJoin", db_column="room_id")
#     created_at = models.DateTimeField(auto_now_add=True)
#     class Meta:
#         db_table = "message"

#     def __str__(self):
#         return self.user_id

#     def last_30_messages(self, room_id):
#         return Message.objects.filter(room_id=room_id).order_by('created_at')[:30]
    
# class ChatRoom(models.Model):
    # user1_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="roomJoin", db_column="username")
    # user2_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="roomJoin", db_column="username")

    # room_id = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="roomJoin", db_column="room_id")
