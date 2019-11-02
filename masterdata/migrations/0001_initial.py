# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-29 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_name', models.CharField(blank=True, max_length=200, null=True)),
                ('d_name', models.CharField(blank=True, max_length=200, null=True)),
                ('actor', models.CharField(blank=True, max_length=200, null=True)),
                ('movie_id', models.IntegerField(blank=True, max_length=200, null=True)),
                ('budget', models.IntegerField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
