# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-03-24 07:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20170323_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='createAt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='desription',
            field=models.TextField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topic',
            name='end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='topic',
            name='start',
            field=models.DateTimeField(),
        ),
    ]
