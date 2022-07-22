from datetime import date
from django.db import models
from AccountApp.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    photo = models.ImageField(null=True, blank=True, upload_to='profile')
    skill = models.CharField(null=True, blank=True, max_length=300)
    introduction = models.CharField(null=True, blank=True, max_length=300)
    interesting_keyword = models.CharField(null=True, blank=True, max_length=300)
    like_place = models.CharField(null=True, blank=True, max_length=300)
    unlike_place = models.CharField(null=True, blank=True, max_length=300)

    def __str__(self):
        return self.user.username

    @property
    def get_photo_url(self):
        # if self.photo and hasattr(self.photo,'url'):
        if self.photo:
            return self.photo.url
        else:
            return "/static/assets/img/photo_add.png"

    @property
    def get_photo_home_url(self):
        if self.photo:
            return self.photo.url
        else:
            return "/static/assets/img/ordinary_profile_photo.png"

class Schedule(models.Model):
<<<<<<< HEAD
    user1 = models.OneToOneField(User, on_delete=models.CASCADE)
    user2 = models.OneToOneField(User, on_delete=models.CASCADE)
    day = models.DateTimeField()
    place = models.CharField(null=True, blank=True)
    topic_list = models.CharField(null=True, blank=True)
=======
    user1 = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.DateTimeField()
    place = models.CharField(null=True, blank=True, max_length=100)
    topic_list = models.CharField(null=True, blank=True, max_length=300)
>>>>>>> 641f3a190a4be592e98ca603519d7caf19349c43

    # user1 user2 day place topic_list

    def __str__(self):
        return self.day, self.place, self.topic_list
