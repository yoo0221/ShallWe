# Generated by Django 4.0.6 on 2022-07-21 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='interesting_keyword',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='introduction',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='like_place',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skill',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='unlike_place',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
