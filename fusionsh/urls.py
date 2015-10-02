# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from runs.views import RunListView, RunnerCreateView, RunnerSuccess
from news.views import NewsIndex, NewDetail, AboutView, ActivitiesView

urlpatterns = [
    url(r'^eventos/(?P<pk>[0-9]+)/$', RunnerCreateView.as_view(), name='runner_create'),
    url(r'^eventos/(?P<pk>[0-9]+)/success/$', RunnerSuccess.as_view(), name='runner_success'),
    url(r'^$', NewsIndex.as_view(), name='news'),
    url(r'^noticias/(?P<slug>\S+)$', NewDetail.as_view(), name="new_detail"),
    url(r'^quienes-somos/', AboutView.as_view(), name='about'),
    url(r'^actividades/', ActivitiesView.as_view(), name='activities'),
    url('^markdown/', include( 'django_markdown.urls')),
    url(r'^sistema/admin/', include(admin.site.urls)),
]
