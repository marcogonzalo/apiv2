# Generated by Django 5.0.3 on 2024-03-07 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authenticate", "0051_delete_legacykey"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Scope",
        ),
        migrations.RemoveField(
            model_name="app",
            name="agreement_version",
        ),
        migrations.RemoveField(
            model_name="app",
            name="algorithm",
        ),
        migrations.RemoveField(
            model_name="app",
            name="app_url",
        ),
        migrations.RemoveField(
            model_name="app",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="app",
            name="description",
        ),
        migrations.RemoveField(
            model_name="app",
            name="private_key",
        ),
        migrations.RemoveField(
            model_name="app",
            name="public_key",
        ),
        migrations.RemoveField(
            model_name="app",
            name="redirect_url",
        ),
        migrations.RemoveField(
            model_name="app",
            name="require_an_agreement",
        ),
        migrations.RemoveField(
            model_name="app",
            name="schema",
        ),
        migrations.RemoveField(
            model_name="app",
            name="slug",
        ),
        migrations.RemoveField(
            model_name="app",
            name="strategy",
        ),
        migrations.RemoveField(
            model_name="app",
            name="webhook_url",
        ),
    ]
