# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-28 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20180301_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobsinfo',
            name='job_requirement',
            field=models.CharField(max_length=2000),
        ),
    ]
