# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-20 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20181220_0956'),
    ]

    operations = [
        migrations.AddField(
            model_name='functionalgroup',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='functionalgroup',
            name='Name',
            field=models.TextField(verbose_name='Functional Group'),
        ),
    ]