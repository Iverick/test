# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-28 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0002_rentalpayment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'ordering': ('price',), 'verbose_name_plural': 'Properties'},
        ),
        migrations.AddField(
            model_name='property',
            name='rent_length',
            field=models.IntegerField(default=10, max_length=3),
            preserve_default=False,
        ),
    ]
