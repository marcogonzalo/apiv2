# Generated by Django 3.2.21 on 2023-09-20 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0032_auto_20230915_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceitemfeature',
            name='title',
            field=models.CharField(default=None,
                                   help_text='Title of the service item',
                                   max_length=30,
                                   null=True),
        ),
    ]