# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-06 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placement', '0003_auto_20170804_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campusdrive',
            name='package',
            field=models.CharField(db_index=True, max_length=10),
        ),
    ]