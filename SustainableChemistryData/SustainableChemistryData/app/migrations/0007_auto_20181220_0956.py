# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-20 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20181220_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='Functional_Group',
            field=models.TextField(verbose_name='Functional Group'),
        ),
        migrations.AlterField(
            model_name='reference',
            name='Name',
            field=models.TextField(null=True, verbose_name='Named Reaction'),
        ),
    ]