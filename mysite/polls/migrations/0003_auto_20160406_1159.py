# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20160406_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Kategorie',
            field=models.CharField(max_length=1000),
        ),
    ]