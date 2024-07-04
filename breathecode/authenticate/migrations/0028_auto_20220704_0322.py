# Generated by Django 3.2.13 on 2022-07-04 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authenticate", "0027_gitpoduser_target_cohort"),
    ]

    operations = [
        migrations.AddField(
            model_name="userinvite",
            name="process_message",
            field=models.CharField(default="", max_length=150),
        ),
        migrations.AddField(
            model_name="userinvite",
            name="process_status",
            field=models.CharField(
                choices=[("PENDING", "Pending"), ("DONE", "Done"), ("ERROR", "Error")], default="PENDING", max_length=7
            ),
        ),
    ]
