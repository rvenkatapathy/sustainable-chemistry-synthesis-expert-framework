# Generated by Django 2.1.5 on 2019-01-30 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20190130_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='namedreaction',
            name='URL',
            field=models.URLField(blank=True),
        ),
    ]
