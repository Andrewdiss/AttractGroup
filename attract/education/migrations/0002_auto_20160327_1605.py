# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 16:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='People',
            new_name='Person',
        ),
        migrations.RenameField(
            model_name='document',
            old_name='person_id',
            new_name='person',
        ),
    ]
