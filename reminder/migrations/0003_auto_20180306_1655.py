# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 16:55
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0002_auto_20180306_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiver',
            name='phone',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message=b'Phone number must be 10 digits.', regex=b'^\\+?1?\\d{10}$')]),
        ),
    ]
