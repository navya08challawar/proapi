# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-01 13:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportcard',
            old_name='sub1',
            new_name='bio',
        ),
        migrations.RenameField(
            model_name='reportcard',
            old_name='sub2',
            new_name='eng',
        ),
        migrations.RenameField(
            model_name='reportcard',
            old_name='sub3',
            new_name='hindi',
        ),
        migrations.RenameField(
            model_name='reportcard',
            old_name='sub4',
            new_name='tel',
        ),
    ]
