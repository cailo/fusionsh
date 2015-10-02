# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'titulo')),
                ('resume', models.TextField(verbose_name=b'resumen')),
                ('body', models.TextField(verbose_name=b'contenido')),
                ('image_new', models.ImageField(upload_to=b'images', verbose_name=b'image')),
                ('slug', models.SlugField(unique=True, max_length=255)),
                ('publish', models.BooleanField(default=True, verbose_name=b'publicado')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'noticia',
                'verbose_name_plural': 'noticias',
            },
            bases=(models.Model,),
        ),
    ]
