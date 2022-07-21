from django.db import models
from django.contrib.auth.models import AbstractUser
# # Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=100, null=True)
    birth = models.DateField(null=True)
    age = models.IntegerField(null=True)
    sex = models.CharField(max_length=5, null=True)
    mother_tongue = models.CharField(max_length=50, null=True)
    address_do = models.CharField(max_length=20, null=True)
    address_sgg = models.CharField(max_length=30, null=True)
    address_emd = models.CharField(max_length=20, null=True)
    nationality = models.CharField(max_length=30, null=True)
    # photo = models.ImageField(null=True, blank=True, upload_to='profile')
    # skill = models.TextField(null=True)
    # introduction = models.TextField(null=True)
    # interesting_keyword = models.TextField(null=True)
    # like_place = models.TextField(null=True)
    # unlike_place = models.TextField(null=True)

    def __str__(self):
        return self.username