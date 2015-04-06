# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo_uploader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='height',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='width',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
