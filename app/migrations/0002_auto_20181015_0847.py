# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-15 05:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Project',
        ),
    ]