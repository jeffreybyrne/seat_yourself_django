# Generated by Django 2.1.5 on 2019-03-13 20:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_auto_20190203_0427'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='last_reservation_time',
            field=models.TimeField(default=datetime.time(20, 41, 12, 352524)),
            preserve_default=False,
        ),
    ]