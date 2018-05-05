# Generated by Django 2.0.3 on 2018-03-25 14:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('perftracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComparisonModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Comparison title', max_length=512)),
                ('author', models.CharField(blank=True, help_text='Comparison author: user@mycompany.localdomain', max_length=128, null=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, help_text='Comparison updated datetime')),
                ('is_public', models.BooleanField(default=False, help_text='Seen to everybody')),
                ('charts_type', models.IntegerField(choices=[(0, 'Auto'), (1, 'No charts'), (2, 'XY-line'), (3, 'XY-line + trend'), (4, 'Bar charts'), (5, 'Bar + trend')], default=0, help_text='Charts type')),
                ('tables_type', models.IntegerField(choices=[(0, 'Auto'), (1, 'Hide all tables'), (2, 'Show all tables')], default=0, help_text='Tables type')),
                ('tests_type', models.IntegerField(choices=[(0, 'Auto'), (1, 'Tests w/o warnings'), (2, 'Tests w/o errors'), (3, 'All tests')], default=0, help_text='Tests type')),
                ('values_type', models.IntegerField(choices=[(0, 'Auto'), (1, 'Average values'), (2, 'Min values'), (3, 'Max values')], default=0, help_text='Values type')),
                ('jobs', models.ManyToManyField(help_text='Jobs', to='perftracker.JobModel')),
                ('project', models.ForeignKey(help_text='Comparison project', on_delete=django.db.models.deletion.CASCADE, to='perftracker.ProjectModel')),
            ],
            options={
                'verbose_name': 'Comparison',
                'verbose_name_plural': 'Comparisons',
            },
        ),
    ]
