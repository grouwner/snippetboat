# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-08 12:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20170408_1445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='author',
            new_name='autore',
        ),
        migrations.RenameField(
            model_name='document',
            old_name='text',
            new_name='testo',
        ),
        migrations.RenameField(
            model_name='document',
            old_name='title',
            new_name='titolo',
        ),
    ]
