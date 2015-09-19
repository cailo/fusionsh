# -*- encoding: utf-8 -*-

from django.views.generic import ListView, CreateView, TemplateView
from runs.forms import RunnerForm
from runs.models import Run, Runner
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class RunListView(ListView):
    """
    """
    model = Run
    template_name = 'base.html'

class RunnerCreateView(CreateView):
    """
    """
    form_class = RunnerForm
    template_name = 'runs/runner_form.html'

    def get_form(self, form_class):
        form = super(RunnerCreateView, self).get_form(form_class)
        form.set_categories(self.kwargs['pk'])
        form.set_distances(self.kwargs['pk'])
        return form 

    def get_context_data(self, **kwargs):
        context = super(RunnerCreateView, self).get_context_data(**kwargs)
        context['run_list'] = Run.objects.all()
        context['rundata'] = Run.objects.get(pk=self.kwargs['pk'])
        #context['run_distances'] = Run.objects.distances.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form = form.instance
        run = Run.objects.get(pk=self.kwargs['pk'])
        #run.decrement_quota()

        distance = form.cleaned_data.get('distance')
        Distance.objects.get(pk=distance).decrement_quota()

        form.run = run
        form.save()
        return super(RunnerCreateView, self).form_valid(form)
        #return self.render_to_response(self.get_context_data(form=form))
        #return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        #return reverse('run_list')
        return reverse('runner_success', args=(self.kwargs['pk'],))

class RunnerSuccess(TemplateView):
    template_name='runs/form_success.html'

    def get_context_data(self, **kwargs):
        context = super(RunnerSuccess, self).get_context_data(**kwargs)
        context['run_list'] = Run.objects.all()
        #context['runnerdata'] = Runner.objects.get(pk=self)
        context['rundata'] = Run.objects.get(pk=self.kwargs['pk'])
        return context
