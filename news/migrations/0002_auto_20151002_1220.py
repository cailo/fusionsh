# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='image_new',
            field=models.ImageField(upload_to=b'images', null=True, verbose_name=b'image', blank=True),
            preserve_default=True,
        ),
    ]
