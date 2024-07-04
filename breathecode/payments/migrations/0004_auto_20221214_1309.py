# Generated by Django 3.2.16 on 2022-12-14 13:09

import breathecode.utils.validators.language
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0003_auto_20221213_0942"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="planserviceitem",
            name="plan_financing",
        ),
        migrations.RemoveField(
            model_name="planserviceitem",
            name="subscription",
        ),
        migrations.CreateModel(
            name="ServiceItemFeature",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("unit_type", models.CharField(choices=[("UNIT", "Unit")], default="UNIT", max_length=10)),
                ("how_many", models.IntegerField(default=-1)),
                (
                    "lang",
                    models.CharField(
                        max_length=5, validators=[breathecode.utils.validators.language.validate_language_code]
                    ),
                ),
                ("description", models.CharField(max_length=255)),
                ("one_line_desc", models.CharField(max_length=30)),
                (
                    "service_item",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="payments.serviceitem"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PlanServiceItemHandler",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "handler",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="payments.planserviceitem"),
                ),
                (
                    "plan_financing",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="payments.planfinancing",
                    ),
                ),
                (
                    "subscription",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="payments.subscription",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="servicestockscheduler",
            name="plan_handler",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="payments.planserviceitemhandler",
            ),
        ),
    ]
