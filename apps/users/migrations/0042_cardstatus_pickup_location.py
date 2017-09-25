# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 04:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0008_auto_20170925_1024'),
        ('users', '0041_auto_20170924_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardstatus',
            name='pickup_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='card_statuses', to='partner.Partner'),
        ),
    ]
