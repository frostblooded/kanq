# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-03-26 06:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_badge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='createAt',
            new_name='createdAt',
        ),
    ]
