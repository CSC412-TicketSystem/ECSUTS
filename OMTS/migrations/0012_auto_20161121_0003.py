# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-21 00:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OMTS', '0011_studentinfo_studentemail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='rankOfTicket',
            field=models.IntegerField(null=True),
        ),
    ]
