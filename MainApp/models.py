from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=5)
    mother_tongue = models.CharField(max_length=50)
    residence = models.CharField(max_length=200)
    nationality = models.CharField(max_length=30)
    profile_photo = models.ImageField(null=True)
    skill = models.TextField(null=True)
    introduction = models.TextField(null=True)
    interesting_keyword = models.TextField(null=True)
    like_place = models.TextField(null=True)
    unnlike_place = models.TextField(null=True)