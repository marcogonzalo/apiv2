# Generated by Django 5.1.2 on 2024-10-22 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mentorship", "0032_mentorshipsession_meta_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mentorshipsession",
            name="meta",
        ),
    ]
