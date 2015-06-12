# -*- encoding: utf-8 -*-

from django import forms
from runs.models import Category, Distance, Run, Runner

class RunnerForm(forms.ModelForm):
    """
    """
    def set_categories(self, run_pk):
        run = Run.objects.get(pk=run_pk)
        category_list = [c.pk for c in run.categories.all()]
        queryset = Category.objects.filter(pk__in=category_list)
        self.fields['category'] = forms.ModelChoiceField(queryset=queryset, label='Categoría')

    def set_distances(self, run_pk):
        run = Run.objects.get(pk=run_pk)
        distance_list = [c.pk for c in run.distances.all()]
        queryset = Distance.objects.filter(pk__in=distance_list)
        self.fields['distance'] = forms.ModelChoiceField(queryset=queryset, label='Distancia')

    def __init__(self, *args, **kwargs):
        super(RunnerForm, self).__init__(*args, **kwargs)
        # assign a (computed, I assume) default value to the choice field
        self.initial['nationality'] = 'AR'

    class Meta:
        model = Runner
        exclude = ('run', 'assigned_numbers')
