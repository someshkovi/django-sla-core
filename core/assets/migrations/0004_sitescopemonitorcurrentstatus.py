# Generated by Django 3.2.4 on 2021-07-06 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20210706_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteScopeMonitorCurrentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=100)),
                ('monitorName', models.CharField(max_length=200)),
                ('monitorMetric', models.CharField(blank=True, max_length=30, null=True)),
                ('lastUpdateTime', models.DateTimeField(blank=True, null=True)),
                ('rstatus', models.IntegerField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=30, null=True)),
                ('displayName', models.CharField(blank=True, max_length=100, null=True)),
                ('ipAddress', models.CharField(blank=True, max_length=30, null=True)),
                ('status', models.CharField(blank=True, default='Active', max_length=20, null=True)),
                ('assignmentGroup', models.CharField(blank=True, max_length=20, null=True)),
                ('os', models.CharField(blank=True, max_length=60, null=True)),
                ('os_version', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
