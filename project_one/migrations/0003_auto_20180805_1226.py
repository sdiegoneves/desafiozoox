# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-05 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_one', '0002_auto_20180805_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='state',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
