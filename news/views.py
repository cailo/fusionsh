from django.views.generic import ListView, CreateView, TemplateView, DetailView
#from runs.forms import RunnerForm
from runs.models import Run, Runner
#from news.models import Entry
from django.http import HttpResponseRedirect
#news
from . import models

#Class News

class NewsIndex(ListView):
    queryset = models.New.objects.published()
    template_name ='news/base.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(NewsIndex, self).get_context_data(**kwargs)
        context['run_list'] = Run.objects.all()
        return context

class NewDetail(DetailView):
    model = models.New
    template_name = "news/new.html"

    def get_context_data(self, **kwargs):
        context = super(NewDetail, self).get_context_data(**kwargs)
        context['run_list'] = Run.objects.all()
        return context


# Class Static
"""
class NewsView(TemplateView):
    template_name='news/base.html'

    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)
        context['run_list'] = Run.objects.all()
        return context
"""

class AboutView(TemplateView):
    template_name='about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['run_list'] = Run.objects.all()
        return context

class ActivitiesView(TemplateView):
    template_name='activities.html'

    def get_context_data(self, **kwargs):
        context = super(ActivitiesView, self).get_context_data(**kwargs)
        context['run_list'] = Run.objects.all()
        return context

