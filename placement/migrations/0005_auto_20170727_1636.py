# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-27 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placement', '0004_auto_20170727_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.SlugField(),
        ),
    ]
