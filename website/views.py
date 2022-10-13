from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'pages/home.html')

def blog(request):
    return render(request, 'pages/blog.html')

def projects(request):
    return render(request, 'pages/projects.html')

def repos(request):
    return render(request, 'pages/repos.html')

