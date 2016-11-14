from django.conf.urls import patterns,url
from MaintTick import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^$', views.Daniel, name='Daniel'),
        )
