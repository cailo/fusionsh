# -*- encoding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse

"""
class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug
"""
class NewQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class New(models.Model):
    title = models.CharField('titulo', max_length=255)
    resume = models.TextField('resumen')
    body = models.TextField('contenido')
    image_new = models.ImageField('image', upload_to='images', null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    publish = models.BooleanField('publicado', default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    #tags = models.ManyToManyField(Tag)

    objects = NewQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("new_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "noticia"
        verbose_name_plural = "noticias"
        ordering = ["-created"]
