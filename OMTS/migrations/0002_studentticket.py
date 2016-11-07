# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 14:47
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('OMTS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentTicket',
            fields=[
                ('ticket_number', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]