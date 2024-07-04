# Generated by Django 3.2.6 on 2021-08-13 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admissions", "0022_specialtymode_syllabus"),
    ]

    operations = [
        migrations.AddField(
            model_name="syllabus",
            name="name",
            field=models.CharField(blank=True, default=None, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name="syllabus",
            name="slug",
            field=models.SlugField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
