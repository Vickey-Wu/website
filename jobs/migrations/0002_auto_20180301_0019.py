# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-28 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobsinfo',
            name='job_requirement',
            field=models.TextField(),
        ),
    ]