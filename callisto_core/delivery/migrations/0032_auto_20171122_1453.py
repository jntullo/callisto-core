# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 14:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0031_auto_20171122_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sentmatchreport',
            name='sentreport_ptr',
        ),
        migrations.DeleteModel(
            name='SentMatchReport',
        ),
    ]
