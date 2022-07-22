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

class Topic(models.Model):
    topic = models.CharField(max_length=200)
    def __str__(self):
        return self.topic

class Schedule(models.Model):
    schedule_mate = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    my_date_field = models.DateField()
    my_time_field = models.TimeField()
    place = models.CharField(null=True, blank=True, max_length=100)
    topic_list = models.ForeignKey(Topic, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.place
