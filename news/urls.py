from django.conf.urls import patterns, url

from news import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]