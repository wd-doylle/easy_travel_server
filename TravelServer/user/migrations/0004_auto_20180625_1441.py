# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-25 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='description',
            field=models.CharField(max_length=8000),
        ),
        migrations.AlterField(
            model_name='route',
            name='route',
            field=models.CharField(max_length=800),
        ),
    ]
