# Generated by Django 3.2.25 on 2024-10-01 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_user',
            new_name='user',
        ),
    ]
