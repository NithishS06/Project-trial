# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-27 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placement', '0005_auto_20170727_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
