# Generated by Django 2.0.3 on 2018-07-01 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perftracker', '0019_auto_20180624_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegressionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Job title', max_length=512)),
                ('tag', models.CharField(help_text='MyProduct-2.0 regression', max_length=512)),
                ('deleted', models.BooleanField(db_index=True, default=False, help_text='True means the Job was deleted')),
            ],
        ),
        migrations.AddField(
            model_name='jobmodel',
            name='regression_tag',
            field=models.CharField(help_text='MyProduct-2.0 regression', max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='regressionmodel',
            name='first_job',
            field=models.ForeignKey(blank=True, help_text='First job', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='regr_first_job', to='perftracker.JobModel'),
        ),
        migrations.AddField(
            model_name='regressionmodel',
            name='last_job',
            field=models.ForeignKey(blank=True, help_text='Last job', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='regr_last_job', to='perftracker.JobModel'),
        ),
        migrations.AddField(
            model_name='regressionmodel',
            name='project',
            field=models.ForeignKey(help_text='Job project', on_delete=django.db.models.deletion.CASCADE, to='perftracker.ProjectModel'),
        ),
    ]
