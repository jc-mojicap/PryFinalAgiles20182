# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-18 22:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
