# Generated by Django 5.0.3 on 2024-04-03 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("assessment", "0005_option_position_question_position"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="is_deleted",
            field=models.BooleanField(
                default=False,
                help_text="Question collected answers cannot not be deleted, they will have this bullet true",
            ),
        ),
    ]
