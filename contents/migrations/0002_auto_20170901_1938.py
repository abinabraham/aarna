# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='price',
            field=models.ImageField(blank=True, null=True, upload_to='static/sliders/', verbose_name='Price Image'),
        ),
        migrations.AddField(
            model_name='slider',
            name='slider1',
            field=models.ImageField(blank=True, null=True, upload_to='static/sliders/', verbose_name='SLider Image'),
        ),
    ]
