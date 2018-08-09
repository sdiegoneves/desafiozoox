# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-09 03:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_one', '0007_auto_20180805_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='creation_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='city',
            name='last_update_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterModelTable(
            name='state',
            table='project_one_state',
        ),
    ]