# Generated by Django 4.2.3 on 2023-09-22 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callback',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 22, 22, 15, 37, 347442)),
        ),
        migrations.AlterField(
            model_name='mynotes',
            name='currunt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 22, 22, 15, 37, 347442)),
        ),
        migrations.AlterField(
            model_name='usersignup',
            name='currunt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 22, 22, 15, 37, 347442)),
        ),
    ]
