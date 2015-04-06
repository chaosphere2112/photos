# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo_uploader', '0002_auto_20150406_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='display',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='photo',
            name='caption',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='height',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='width',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
