# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-19 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('key', '0002_auto_20170719_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributedkey',
            name='key',
            field=models.TextField(blank=True, help_text='Leave blank for auto-generation.'),
        ),
    ]
