# Generated by Django 3.2.16 on 2023-02-28 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0055_cohort_available_as_saas'),
        ('payments', '0020_auto_20230223_0634'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planfinancing',
            old_name='cohort_selected',
            new_name='selected_cohort',
        ),
        migrations.RenameField(
            model_name='planfinancing',
            old_name='event_type_set_selected',
            new_name='selected_event_type_set',
        ),
        migrations.RenameField(
            model_name='planfinancing',
            old_name='mentorship_service_set_selected',
            new_name='selected_mentorship_service_set',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='cohort_selected',
            new_name='selected_cohort',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='event_type_set_selected',
            new_name='selected_event_type_set',
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='mentorship_service_set_selected',
            new_name='selected_mentorship_service_set',
        ),
        migrations.RemoveField(
            model_name='consumable',
            name='event_type',
        ),
        migrations.RemoveField(
            model_name='consumable',
            name='mentorship_service',
        ),
        migrations.RemoveField(
            model_name='planserviceitem',
            name='cohort_pattern',
        ),
        migrations.RemoveField(
            model_name='planserviceitem',
            name='cohorts',
        ),
        migrations.RemoveField(
            model_name='planserviceitem',
            name='event_type_sets',
        ),
        migrations.RemoveField(
            model_name='planserviceitem',
            name='mentorship_service_sets',
        ),
        migrations.AddField(
            model_name='consumable',
            name='event_type_set',
            field=models.ForeignKey(blank=True,
                                    default=None,
                                    help_text='Event type which the consumable belongs to',
                                    null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    to='payments.eventtypeset'),
        ),
        migrations.AddField(
            model_name='consumable',
            name='mentorship_service_set',
            field=models.ForeignKey(blank=True,
                                    default=None,
                                    help_text='Mentorship service which the consumable belongs to',
                                    null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    to='payments.mentorshipserviceset'),
        ),
        migrations.AddField(
            model_name='plan',
            name='available_cohorts',
            field=models.ManyToManyField(blank=True,
                                         help_text='Available cohorts to be sold in this this service and plan',
                                         to='admissions.Cohort'),
        ),
        migrations.AddField(
            model_name='plan',
            name='available_event_type_sets',
            field=models.ManyToManyField(
                blank=True,
                help_text='Available mentorship service sets to be sold in this service and plan',
                to='payments.EventTypeSet'),
        ),
        migrations.AddField(
            model_name='plan',
            name='available_mentorship_service_sets',
            field=models.ManyToManyField(
                blank=True,
                help_text='Available mentorship service sets to be sold in this service and plan',
                to='payments.MentorshipServiceSet'),
        ),
        migrations.AddField(
            model_name='plan',
            name='cohort_pattern',
            field=models.CharField(blank=True,
                                   default=None,
                                   help_text='Cohort pattern to find cohorts to be sold in this plan',
                                   max_length=80,
                                   null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='type',
            field=models.CharField(choices=[('COHORT', 'Cohort'), ('MENTORSHIP_SERVICE_SET', 'Mentorship service set'),
                                            ('EVENT_TYPE_SET', 'Event type set')],
                                   default='COHORT',
                                   help_text='Service type',
                                   max_length=22),
        ),
        migrations.AlterField(
            model_name='consumable',
            name='cohort',
            field=models.ForeignKey(blank=True,
                                    default=None,
                                    help_text='Cohort which the consumable belongs to',
                                    null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    to='admissions.cohort'),
        ),
        migrations.CreateModel(
            name='AcademyService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_per_unit', models.FloatField(default=1, help_text='Price per unit (e.g. 1, 2, 3, ...)')),
                ('cohort_patterns',
                 models.JSONField(blank=True,
                                  default=[],
                                  help_text='Array of cohort patterns to find cohorts to be sold in this plan')),
                ('academy',
                 models.ForeignKey(help_text='Academy',
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='admissions.academy')),
                ('available_cohorts',
                 models.ManyToManyField(blank=True,
                                        help_text='Available cohorts to be sold in this this service and plan',
                                        to='admissions.Cohort')),
                ('available_event_type_sets',
                 models.ManyToManyField(
                     blank=True,
                     help_text='Available mentorship service sets to be sold in this service and plan',
                     to='payments.EventTypeSet')),
                ('available_mentorship_service_sets',
                 models.ManyToManyField(
                     blank=True,
                     help_text='Available mentorship service sets to be sold in this service and plan',
                     to='payments.MentorshipServiceSet')),
                ('currency',
                 models.ForeignKey(help_text='Currency',
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='payments.currency')),
                ('service',
                 models.OneToOneField(help_text='Service',
                                      on_delete=django.db.models.deletion.CASCADE,
                                      to='payments.service')),
            ],
        ),
    ]
