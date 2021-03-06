# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='partners/'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='slug',
            field=models.SlugField(blank=True, help_text='Leave empty/unchanged for default slug.', max_length=255, null=True),
        ),
    ]
