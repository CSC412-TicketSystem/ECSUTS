# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-21 00:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OMTS', '0012_auto_20161121_0003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentinfo',
            old_name='first_name',
            new_name='student_name',
        ),
        migrations.RemoveField(
            model_name='studentinfo',
            name='last_name',
        ),
    ]
