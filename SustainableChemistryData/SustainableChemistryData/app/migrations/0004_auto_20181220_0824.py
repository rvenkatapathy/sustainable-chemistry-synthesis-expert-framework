# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-20 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20181219_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reference',
            name='Named_Reaction',
        ),
        migrations.AddField(
            model_name='reference',
            name='Name',
            field=models.TextField(null=True, verbose_name='Named Reaction'),
        ),
        migrations.AlterField(
            model_name='namedreaction',
            name='Functional_Group',
            field=models.TextField(verbose_name='Functional Group'),
        ),
        migrations.AlterField(
            model_name='reference',
            name='Functional_Group',
            field=models.TextField(verbose_name='Functional Group'),
        ),
    ]
