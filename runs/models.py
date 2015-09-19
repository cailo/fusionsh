# -*- encoding: utf-8 -*-

from django.db import models
from django_countries.fields import CountryField

class Category(models.Model):
    """
    """
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'

class Distance(models.Model):
    """
    """
    name = models.CharField(max_length=32)
    price = models.CharField(max_length=32)
    quota = models.PositiveIntegerField('cupo')

    def __str__(self):
        return '{} - {} - {}'.format(self.name, self.price, self.quota)
    
    def is_quota(self):
        if self.quota > 0:
            return True
        else:
            return False

    def decrement_quota(self):
        self.quota -= 1
        self.save()    

    class Meta:
        verbose_name = 'distancia'
        verbose_name_plural = 'distancias'

class Run(models.Model):
    """
    """
    STATE_CHOICES = (
        (1, 'Activado'),
        (2, 'Desactivado')
    )
    name = models.CharField('nombre', max_length=64)
    logotype = models.ImageField('logotipo', upload_to='banners')
    banner = models.ImageField('banner', upload_to='banners')
    date_text = models.CharField('fecha texto', max_length=128)
    date_limit = models.CharField('fecha limite', max_length=128)
    description = models.TextField('descripción',)
    date = models.DateTimeField('fecha')
    place = models.CharField('lugar', max_length=64)
    distances = models.ManyToManyField(Distance, verbose_name='distancias')
    banner2 = models.ImageField('banner2', upload_to='banners')
    advertising = models.FileField('publicidad', upload_to='archives', null=True, blank=True)
    timetable = models.FileField('cronograma', upload_to='archives', null=True, blank=True)
    demarcation = models.FileField('deslinde', upload_to='archives', null=True, blank=True)
    medical_record = models.FileField('ficha medica', upload_to='archives', null=True, blank=True)
    regulation = models.FileField('reglamento', upload_to='archives', null=True, blank=True)
    travel = models.FileField('recorrido', upload_to='archives', null=True, blank=True)
    accommodation = models.FileField('alojamiento', upload_to='archives', null=True, blank=True)
    how_to_get = models.FileField('como llegar', upload_to='archives', null=True, blank=True)
    payment_method = models.CharField('método de pago', max_length=64, null=True, blank=True)
    payment_place = models.CharField('lugar de pago', max_length=64, null=True, blank=True)
    categories = models.ManyToManyField(Category, verbose_name='categorías')
    state = models.PositiveIntegerField('estado', choices=STATE_CHOICES)
    results_general = models.FileField('resuldos general', upload_to='archives', null=True, blank=True)
    results_category = models.FileField('resultados x categoria', upload_to='archives', null=True, blank=True)
    gallery_link = models.CharField('galeria', max_length=255, null=True, blank=True)

    def __str__(self):
        #return '{} - {}'.format(self.date.strftime('%Y/%m/%d - %H:%M'), self.distance)
        return '{}'.format(self.name)
    
    def get_absolute_url(self):
	return "/carreras/%i/" % self.id    
    
    #def decrement_quota(self):
    #    self.quota -= 1
    #    self.save()
    #    if self.quota == 0:
    #        self.state = 2
    #        self.save()
    #        return

    class Meta:
        verbose_name = 'carrera'
        verbose_name_plural = 'carreras'

class Runner(models.Model):
    """
    """
    GENDER_CHOICES = (
        (1, 'Masculino'),
        (2, 'Femenino')
    )
    SIZE_CHOICES = (
        (1, 'XS'),
        (2, 'S'),
        (3, 'M'),
        (4, 'L'),
        (5, 'XL'),
        (6, 'XXL'),
    )
    run = models.ForeignKey(Run, related_name='runners', verbose_name='carrera')
    firstname = models.CharField('nombre/s', max_length=64)
    lastname = models.CharField('apellido/s', max_length=64)
    document = models.CharField('n° de documento', max_length=32)
    birthday = models.DateField('fecha de nacimiento')
    gender = models.PositiveIntegerField('sexo', choices=GENDER_CHOICES)
    nationality = CountryField('pais de naciomiento', default='AR')
    address = models.CharField('dirección', max_length=64)
    phone = models.CharField('teléfono', max_length=64)
    emergency_contact = models.CharField('contacto de emergencia', max_length=64)
    email = models.EmailField('correo elecrónico')
    group = models.CharField('agrupación', max_length=64, null=True, blank=True)
    distance = models.ForeignKey(Distance, related_name='runners_distance', verbose_name='distancia')
    category = models.ForeignKey(Category, related_name='runners_category', verbose_name='categoría')
    size = models.PositiveIntegerField('talle de remera', choices=SIZE_CHOICES)
    assigned_numbers = models.CharField('numero', max_length=6, null=True, blank=True)

    def __str__(self):
        return '{} - {} {}'.format(self.document, self.firstname, self.lastname)

    def get_absolute_url(self):
        return "/carreras/%i/" % self.id

    class Meta:
        verbose_name = 'corredor'
        verbose_name_plural = 'corredores'
