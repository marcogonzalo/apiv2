# Generated by Django 3.1.6 on 2021-02-20 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0008_monitorscript'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('LOADING', 'Loading'), ('OPERATIONAL', 'Operational'), ('MINOR', 'Minor'),
                                            ('CRITICAL', 'Critical')],
                                   default='OPERATIONAL',
                                   max_length=20),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='status',
            field=models.CharField(choices=[('LOADING', 'Loading'), ('OPERATIONAL', 'Operational'), ('MINOR', 'Minor'),
                                            ('CRITICAL', 'Critical')],
                                   default='OPERATIONAL',
                                   max_length=20),
        ),
        migrations.AlterField(
            model_name='monitorscript',
            name='status',
            field=models.CharField(choices=[('LOADING', 'Loading'), ('OPERATIONAL', 'Operational'), ('MINOR', 'Minor'),
                                            ('CRITICAL', 'Critical')],
                                   default='OPERATIONAL',
                                   max_length=20),
        ),
    ]
