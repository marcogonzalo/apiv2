# Generated by Django 3.2.18 on 2023-05-12 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("admissions", "0056_auto_20230317_1657"),
        ("mentorship", "0020_alter_mentorshipservice_language"),
    ]

    operations = [
        migrations.CreateModel(
            name="CalendlyOrganization",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("username", models.CharField(help_text="Calendly username", max_length=100)),
                ("access_token", models.TextField(blank=True, default=None, null=True)),
                ("hash", models.CharField(max_length=40, unique=True)),
                (
                    "sync_status",
                    models.CharField(
                        choices=[
                            ("PENDING", "Pending"),
                            ("PERSISTED", "Persisted"),
                            ("ERROR", "Error"),
                            ("WARNING", "Warning"),
                            ("SYNCHED", "Synched"),
                        ],
                        default="PENDING",
                        help_text="One of: PENDING, PERSISTED or ERROR depending on how the calendly sync status",
                        max_length=9,
                    ),
                ),
                ("sync_desc", models.TextField(blank=True, default=None, max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "academy",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="admissions.academy"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CalendlyWebhook",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("organization_hash", models.CharField(max_length=50)),
                ("created_by", models.CharField(max_length=2500)),
                ("event", models.CharField(max_length=100)),
                ("called_at", models.DateTimeField()),
                ("payload", models.JSONField()),
                (
                    "status",
                    models.CharField(
                        choices=[("PENDING", "Pending"), ("DONE", "Done"), ("ERROR", "Error")],
                        default="PENDING",
                        max_length=9,
                    ),
                ),
                ("status_text", models.CharField(blank=True, default=None, max_length=255, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "organization",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mentorship.calendlyorganization",
                    ),
                ),
            ],
        ),
    ]
