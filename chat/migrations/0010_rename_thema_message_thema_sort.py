# Generated by Django 4.1 on 2022-08-19 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_message_promise_address_message_promise_confirmed_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='thema',
            new_name='thema_sort',
        ),
    ]