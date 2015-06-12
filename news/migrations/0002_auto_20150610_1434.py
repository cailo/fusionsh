# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'titulo')),
                ('body', models.TextField(verbose_name=b'contenido')),
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
        migrations.RemoveField(
            model_name='entry',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
