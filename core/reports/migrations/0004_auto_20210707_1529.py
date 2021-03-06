# Generated by Django 3.2.4 on 2021-07-07 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_alter_slaachievedoverview_slapoint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slapoint',
            name='slaPoint',
            field=models.CharField(max_length=5),
        ),
        migrations.AddConstraint(
            model_name='slapoint',
            constraint=models.UniqueConstraint(fields=('slaPoint',), name='slaPoint'),
        ),
    ]
