# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-14 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConferenceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conference_name', models.CharField(default='', max_length=100)),
                ('begin_time', models.DateField()),
                ('end_time', models.DateField()),
                ('host_address', models.CharField(default='', max_length=255)),
                ('description', models.CharField(default='', max_length=255)),
            ],
        ),
    ]