# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from runs.views import RunListView, RunnerCreateView, RunnerSuccess
from news.views import NewsIndex, NewDetail, AboutView, ActivitiesView

urlpatterns = [
    url(r'^carrera/(?P<pk>[0-9]+)/$', RunnerCreateView.as_view(), name='runner_create'),
    url(r'^carrera/(?P<pk>[0-9]+)/success/$', RunnerSuccess.as_view(), name='runner_success'),
    url(r'^$', NewsIndex.as_view(), name='news'),
    url(r'^news/(?P<slug>\S+)$', NewDetail.as_view(), name="new_detail"),
    url(r'^about/', AboutView.as_view(), name='about'),
    url(r'^activities/', ActivitiesView.as_view(), name='activities'),
    url('^markdown/', include( 'django_markdown.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
