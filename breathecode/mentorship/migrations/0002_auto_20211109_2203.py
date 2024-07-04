# Generated by Django 3.2.7 on 2021-11-09 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admissions", "0025_merge_20211018_2259"),
        ("mentorship", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="mentorprofile",
            name="booking_url",
            field=models.URLField(
                blank=True,
                default=None,
                help_text="URL where this mentor profile can be booked, E.g: calendly.com/my_username",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="mentorprofile",
            name="online_meeting_url",
            field=models.URLField(
                blank=True,
                default=None,
                help_text="If set, it will be default for all session's unless the session.online_meeting_url is set",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="mentorprofile",
            name="slug",
            field=models.SlugField(
                default=None,
                help_text="Will be used as unique public booking URL with the students, for example: 4geeks.com/meet/bob",
                max_length=150,
                unique=True,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="mentorprofile",
            name="syllabus",
            field=models.ManyToManyField(
                blank=True,
                default=None,
                help_text="What syllabis is this mentor going to be menting to?",
                null=True,
                to="admissions.Syllabus",
            ),
        ),
        migrations.AddField(
            model_name="mentorprofile",
            name="timezone",
            field=models.CharField(
                default=None,
                help_text="Knowing the mentor's timezone helps with more accurrate booking",
                max_length=50,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="mentorshipsession",
            name="ends_at",
            field=models.DateTimeField(blank=True, default=None, help_text="Scheduled end date", null=True),
        ),
        migrations.AddField(
            model_name="mentorshipsession",
            name="starts_at",
            field=models.DateTimeField(blank=True, default=None, help_text="Scheduled start date", null=True),
        ),
        migrations.AlterField(
            model_name="mentorprofile",
            name="email",
            field=models.CharField(
                blank=True,
                default=None,
                help_text="Only use this if the user does not exist on breathecode already",
                max_length=150,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="mentorprofile",
            name="name",
            field=models.CharField(blank=True, default=None, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name="mentorprofile",
            name="token",
            field=models.CharField(
                help_text="Used for inviting the user to become a mentor", max_length=255, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="mentorshipsession",
            name="ended_at",
            field=models.DateTimeField(
                blank=True, default=None, help_text="Real start date (only if it started)", null=True
            ),
        ),
        migrations.AlterField(
            model_name="mentorshipsession",
            name="online_meeting_url",
            field=models.URLField(
                blank=True, default=None, help_text="Overrides the mentor.online_meeting_url if set", null=True
            ),
        ),
        migrations.AlterField(
            model_name="mentorshipsession",
            name="online_recording_url",
            field=models.URLField(
                blank=True,
                default=None,
                help_text="We encourace the mentors to record the session and share them with the students",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="mentorshipsession",
            name="started_at",
            field=models.DateTimeField(
                blank=True, default=None, help_text="Real start date (only if it started)", null=True
            ),
        ),
        migrations.AlterField(
            model_name="mentorshipsession",
            name="status",
            field=models.CharField(
                choices=[("PENDING", "Pending"), ("COMPLETED", "Completed"), ("FAILED", "Failed")],
                default="PENDING",
                help_text="Options are: PENDINGCOMPLETEDFAILED",
                max_length=15,
            ),
        ),
    ]
