# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 16:37
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiver',
            name='phone',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message=b'Phone number must be 10 digits.', regex=b'^\\+?1?\\d{10}$')]),
        ),
    ]
