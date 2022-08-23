# Generated by Django 3.2.12 on 2022-04-02 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0013_issue_status_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='status',
            field=models.CharField(choices=[('DUE', 'Due'), ('APPROVED', 'Approved'), ('IGNORED', 'Ignored'),
                                            ('PAID', 'Paid')],
                                   default='DUE',
                                   max_length=20),
        ),
    ]
