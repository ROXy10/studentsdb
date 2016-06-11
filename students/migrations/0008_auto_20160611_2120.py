# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-11 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_auto_20160611_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='title',
        ),
        migrations.AddField(
            model_name='exam',
            name='subject',
            field=models.CharField(default='', max_length=256, verbose_name='\u041f\u0440\u0435\u0434\u043c\u0435\u0442'),
            preserve_default=False,
        ),
    ]
