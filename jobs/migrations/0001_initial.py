# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-23 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=30)),
                ('job_salary', models.CharField(max_length=30)),
                ('job_requirement', models.TextField()),
                ('job_addr', models.CharField(max_length=100)),
                ('job_exp', models.CharField(max_length=20)),
                ('job_edu', models.CharField(max_length=20)),
                ('job_tags', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('company_employee_num', models.IntegerField()),
                ('company_type', models.CharField(max_length=30)),
            ],
        ),
    ]
