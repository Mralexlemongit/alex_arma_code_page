from importlib.resources import path
from xml.etree.ElementInclude import include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.cv, name='home'),
    path('cv', views.cv, name='cv'),
    path('page_info', views.page_info, name='page_info'),
    path('blog', views.blog, name='blog'),
    path('repositories', views.repos, name='repos'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
]