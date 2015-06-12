# -*- encoding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from runs.views import RunListView, RunnerCreateView, RunnerSuccess
from news.views import NewsIndex, NewDetail, AboutView, ActivitiesView
#from fusionsh.news.feeds import LatestPosts

urlpatterns = [
    #url(r'^$', RunListView.as_view(), name='run_list'),
    url(r'^carrera/(?P<pk>[0-9]+)/$', RunnerCreateView.as_view(), name='runner_create'),
    url(r'^carrera/(?P<pk>[0-9]+)/success/$', RunnerSuccess.as_view(), name='runner_success'),
    #url(r'^about/', TemplateView.as_view(template_name="about.html")),
    #url(r'^news/', NewsView.as_view(), name='news'),
    #url(r'^feed/$', feed.LatestPosts(), name="feed"),
    #url(r'^feed/$', LatestPosts()),
    #url(r'^news/$', BlogIndex.as_view(), name='news'),
    url(r'^$', NewsIndex.as_view(), name='news'),
    url(r'^news/(?P<slug>\S+)$', NewDetail.as_view(), name="new_detail"),
    url(r'^about/', AboutView.as_view(), name='about'),
    url(r'^activities/', ActivitiesView.as_view(), name='activities'),
    url('^markdown/', include( 'django_markdown.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
