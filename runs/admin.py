# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField

from import_export.admin import ImportExportModelAdmin
from django.forms import CheckboxSelectMultiple
from runs.models import Category, Distance, Run, Runner

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Distance)
class DistanceAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

@admin.register(Run)
class RunAdmin(MarkdownModelAdmin):
    list_filter = ('name', 'state')
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

@admin.register(Runner)
class RunnerAdmin(ImportExportModelAdmin):
    search_fields = ['firstname', 'lastname', 'document']
    list_filter = ('run__name', 'category', 'gender', 'distance', 'nationality')
    list_display = ('firstname', 'lastname', 'document', 'gender', 'distance', 'category')
    #list_display = ('firstname', 'lastname', 'document', 'gender', 'distance', 'get_name')
    def get_name(self, obj):
        return obj.run.name
    get_name.admin_order_field  = 'run'  
    get_name.short_description = 'Carrera'

#class RunnerInline(admin.TabularInline):
#    model = Runner

#class RunAdmin(admin.ModelAdmin):
#    inline = [
#        RunnerInline,
#    ]


#admin.site.register(RunAdmin, Run)
