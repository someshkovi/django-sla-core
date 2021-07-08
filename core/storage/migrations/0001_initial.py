# Generated by Django 3.2.4 on 2021-07-06 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrimaryStorageModuleStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storageUnit', models.CharField(max_length=20)),
                ('storageModule', models.CharField(max_length=20)),
                ('timeNow', models.DateTimeField()),
                ('dateToday', models.DateField()),
                ('status', models.PositiveIntegerField(choices=[(1, 'noError'), (2, 'acute'), (3, 'serious'), (4, 'moderate'), (5, 'service')])),
                ('nonCritical', models.BooleanField(blank=True, default=0, null=True)),
            ],
            options={
                'verbose_name': 'Primary Storage Module status',
                'verbose_name_plural': 'Primary Storage Module status',
            },
        ),
        migrations.CreateModel(
            name='PrimaryStroageTraps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storageUnit', models.CharField(max_length=20)),
                ('alertId', models.CharField(blank=True, max_length=20, null=True)),
                ('trapId', models.PositiveIntegerField(blank=True, null=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('message', models.CharField(blank=True, max_length=250, null=True)),
                ('acknowledge', models.BooleanField(default=0)),
                ('resolved', models.BooleanField(default=0)),
                ('nonCritical', models.BooleanField(default=0)),
                ('note', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'Primary Storage Traps',
                'verbose_name_plural': 'Primary Storage Traps',
            },
        ),
        migrations.AddConstraint(
            model_name='primarystroagetraps',
            constraint=models.UniqueConstraint(fields=('storageUnit', 'trapId', 'date', 'time', 'message'), name='unique trap'),
        ),
        migrations.AddConstraint(
            model_name='primarystoragemodulestatus',
            constraint=models.UniqueConstraint(fields=('storageUnit', 'storageModule', 'timeNow'), name='unique status'),
        ),
    ]
