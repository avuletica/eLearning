# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='file',
            field=models.FileField(default='', upload_to=b''),
        ),
    ]
