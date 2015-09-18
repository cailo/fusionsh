# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'categor\xeda',
                'verbose_name_plural': 'categor\xedas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'distancia',
                'verbose_name_plural': 'distancias',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name=b'nombre')),
                ('logotype', models.ImageField(upload_to=b'banners', verbose_name=b'logotipo')),
                ('banner', models.ImageField(upload_to=b'banners', verbose_name=b'banner')),
                ('date_text', models.CharField(max_length=128, verbose_name=b'fecha texto')),
                ('date_limit', models.CharField(max_length=128, verbose_name=b'fecha limite')),
                ('description', models.TextField(verbose_name=b'descripci\xc3\xb3n')),
                ('date', models.DateTimeField(verbose_name=b'fecha')),
                ('quota', models.PositiveIntegerField(verbose_name=b'cupo')),
                ('place', models.CharField(max_length=64, verbose_name=b'lugar')),
                ('price', models.DecimalField(null=True, verbose_name=b'precio', max_digits=6, decimal_places=2, blank=True)),
                ('banner2', models.ImageField(upload_to=b'banners', verbose_name=b'banner2')),
                ('advertising', models.FileField(upload_to=b'archives', null=True, verbose_name=b'publicidad', blank=True)),
                ('timetable', models.FileField(upload_to=b'archives', null=True, verbose_name=b'cronograma', blank=True)),
                ('demarcation', models.FileField(upload_to=b'archives', null=True, verbose_name=b'deslinde', blank=True)),
                ('medical_record', models.FileField(upload_to=b'archives', null=True, verbose_name=b'ficha medica', blank=True)),
                ('regulation', models.FileField(upload_to=b'archives', null=True, verbose_name=b'reglamento', blank=True)),
                ('travel', models.FileField(upload_to=b'archives', null=True, verbose_name=b'recorrido', blank=True)),
                ('accommodation', models.FileField(upload_to=b'archives', null=True, verbose_name=b'alojamiento', blank=True)),
                ('how_to_get', models.FileField(upload_to=b'archives', null=True, verbose_name=b'como llegar', blank=True)),
                ('payment_method', models.CharField(max_length=64, null=True, verbose_name=b'm\xc3\xa9todo de pago', blank=True)),
                ('payment_place', models.CharField(max_length=64, null=True, verbose_name=b'lugar de pago', blank=True)),
                ('state', models.PositiveIntegerField(verbose_name=b'estado', choices=[(1, b'Activado'), (2, b'Desactivado')])),
                ('results_general', models.FileField(upload_to=b'archives', null=True, verbose_name=b'resuldos general', blank=True)),
                ('results_category', models.FileField(upload_to=b'archives', null=True, verbose_name=b'resultados x categoria', blank=True)),
                ('gallery_link', models.CharField(max_length=255, null=True, verbose_name=b'galeria', blank=True)),
                ('categories', models.ManyToManyField(to='runs.Category', verbose_name=b'categor\xc3\xadas')),
                ('distances', models.ManyToManyField(to='runs.Distance', verbose_name=b'distancias')),
            ],
            options={
                'verbose_name': 'carrera',
                'verbose_name_plural': 'carreras',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Runner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=64, verbose_name=b'nombre/s')),
                ('lastname', models.CharField(max_length=64, verbose_name=b'apellido/s')),
                ('document', models.CharField(max_length=32, verbose_name=b'n\xc2\xb0 de documento')),
                ('birthday', models.DateField(verbose_name=b'fecha de nacimiento')),
                ('gender', models.PositiveIntegerField(verbose_name=b'sexo', choices=[(1, b'Masculino'), (2, b'Femenino')])),
                ('nationality', django_countries.fields.CountryField(default=b'AR', max_length=2, verbose_name=b'pais de naciomiento')),
                ('address', models.CharField(max_length=64, verbose_name=b'direcci\xc3\xb3n')),
                ('phone', models.CharField(max_length=64, verbose_name=b'tel\xc3\xa9fono')),
                ('emergency_contact', models.CharField(max_length=64, verbose_name=b'contacto de emergencia')),
                ('email', models.EmailField(max_length=75, verbose_name=b'correo elecr\xc3\xb3nico')),
                ('group', models.CharField(max_length=64, null=True, verbose_name=b'agrupaci\xc3\xb3n', blank=True)),
                ('size', models.PositiveIntegerField(verbose_name=b'talle de remera', choices=[(1, b'XS'), (2, b'S'), (3, b'M'), (4, b'L'), (5, b'XL'), (6, b'XXL')])),
                ('assigned_numbers', models.CharField(max_length=6, null=True, verbose_name=b'numero', blank=True)),
                ('category', models.ForeignKey(related_name='runners_category', verbose_name=b'categor\xc3\xada', to='runs.Category')),
                ('distance', models.ForeignKey(related_name='runners_distance', verbose_name=b'distancia', to='runs.Distance')),
                ('run', models.ForeignKey(related_name='runners', verbose_name=b'carrera', to='runs.Run')),
            ],
            options={
                'verbose_name': 'corredor',
                'verbose_name_plural': 'corredores',
            },
            bases=(models.Model,),
        ),
    ]
