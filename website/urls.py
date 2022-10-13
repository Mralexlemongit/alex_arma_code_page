from importlib.resources import path
from xml.etree.ElementInclude import include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('home', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('repositories', views.repos, name='repos'),
    path('projects', views.projects, name='projects'),
]