# Generated by Django 3.2 on 2021-04-26 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authenticate", "0020_userinvite_sent_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="DeviceId",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=40)),
                ("key", models.CharField(max_length=64)),
            ],
        ),
    ]
