# -*- coding: utf-8 -*-
from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField
from news.models import New

@admin.register(New)
class NewAdmin(MarkdownModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

