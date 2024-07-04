# Generated by Django 3.1.1 on 2020-10-05 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authenticate", "0007_profile_userautentication"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="bio",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="blog",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="twitter_username",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
