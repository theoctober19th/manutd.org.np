# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 06:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0051_auto_20170928_1236'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='competition',
            options={'ordering': ('-order',)},
        ),
    ]
