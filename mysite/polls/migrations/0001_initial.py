# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-06 08:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Preis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Neuer_Preis', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Alter_Preis', models.DecimalField(decimal_places=2, max_digits=10)),
                ('datumzeit', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product', models.CharField(max_length=1000)),
                ('GuenstigsterPreis', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('AktuellerPreis', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('Kategorie', models.CharField(default='', max_length=400)),
            ],
        ),
        migrations.AddField(
            model_name='preis',
            name='Product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Product'),
        ),
    ]
