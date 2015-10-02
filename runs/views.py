# -*- encoding: utf-8 -*-

from django.views.generic import ListView, CreateView, TemplateView
from runs.forms import RunnerForm
from runs.models import Run, Runner
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail


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
        return context

    def form_valid(self, form):
        distance = form.cleaned_data['distance']
        distance.decrement_quota()

        run = Run.objects.get(pk=self.kwargs['pk'])
        listpayment = run.payment_place
        
        subject = 'Inscripciones %s - Fusion' % (
            run.name
            )

        message = '%s %s te registraste correctamente en la carrera %s.\n\n Datos para pagar a traves de deposito bancario. \n\n FUSION S.H. \n CUIT: 30-71262960-2 \n Banco Supervielle. \n Nro. de Cuenta en pesos: ⁠⁠02267446-001 \n CBU: 0270101710022674460013 \n\n Cualquier duda o inconveniente comunicarse: \n Cel.: 2664488446 / email: info@fusionsh.com.ar \n\n Fusion (mente+cuerpo) \n\n Por favor no responder este mail.' % (
            form.cleaned_data['firstname'],
            form.cleaned_data['lastname'],
            run.name,
            )

        send_mail(
            subject,
            message,
            'no-reply@fusionsh.com.ar',
            [form.cleaned_data['email']],
            fail_silently=False
            )

        form = form.instance
        form.run = run
        form.save()

        return super(RunnerCreateView, self).form_valid(form)

    def get_success_url(self):
        #return reverse('run_list')
        return reverse('runner_success', args=(self.kwargs['pk'],))

class RunnerSuccess(TemplateView):
    template_name='runs/form_success.html'

    def get_context_data(self, **kwargs):
        context = super(RunnerSuccess, self).get_context_data(**kwargs)
        context['run_list'] = Run.objects.all()
        #context['runnerdata'] = Runner.objects.get(pk=self.kwargs['runner_pk'])
        context['rundata'] = Run.objects.get(pk=self.kwargs['pk'])
        return context
