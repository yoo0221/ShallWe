# Generated by Django 4.0.6 on 2022-07-21 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountApp', '0010_rename_unnlike_place_user_unlike_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='blog_photo'),
        ),
    ]