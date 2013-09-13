from django.conf.urls import patterns, url

from expenses import views

urlpatterns = patterns('',
  url(r'^$', views.index, name="index"),
  url(r'^new$', views.new, name="new"),
  url(r'^create$', views.create, name="create") #POST
)
