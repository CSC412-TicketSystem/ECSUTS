# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('resid_hall', models.TextField()),
                ('room_num', models.CharField(max_length=10)),
                ('occupancy', models.CharField(max_length=1)),
                ('issues', models.CharField(choices=[('BD', 'Bed'), ('DSK', 'Desk'), ('DSSR', 'Dresser'), ('CLST', 'Closet'), ('MTTRESS', 'Mattress'), ('WNDOW', 'Window'), ('WNDOWBLNDS', 'Window_Blinds'), ('WLLS', 'Walls'), ('MCROFRDGE', 'Microfridge'), ('MCROWVE', 'Microwave'), ('DOORS', 'Doors'), ('FLOORS', 'Floors'), ('LCKS', 'Locks'), ('BTHROOMSHWR', 'Bathroom_Shower'), ('BTHROOMWLLS', 'Bathroom_walls'), ('BTHROOMTLIT', 'Bathroom_toilet'), ('AC', 'Air_Conditioning_Unit'), ('SNKMRROR', 'Sink/Mirror'), ('ELECTOUTLETS', 'Electrical_Outlets'), ('LGHTS', 'Lights')], default='BD', max_length=12)),
                ('rankOfTicket', models.CharField(max_length=1)),
                ('briefDescription', models.TextField()),
            ],
        ),
    ]
