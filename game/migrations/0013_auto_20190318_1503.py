# Generated by Django 2.1.5 on 2019-03-18 15:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_auto_20190317_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playeruser',
            name='regTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 18, 15, 3, 50, 607597, tzinfo=utc)),
        ),
    ]
