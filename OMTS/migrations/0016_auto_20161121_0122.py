# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-21 01:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OMTS', '0015_auto_20161121_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='occupancy',
            field=models.CharField(max_length=6),
        ),
    ]
