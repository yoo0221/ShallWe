from django.contrib import admin

from MainApp.models import UserProfile, Schedule

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Schedule)