from django.shortcuts import render
from django.http import HttpResponse

def cv(request):
    return render(request, 'pages/cv.html')

def blog(request):
    return render(request, 'pages/blog.html')

def projects(request):
    return render(request, 'pages/projects.html')

def repos(request):
    return render(request, 'pages/repos.html')

def contact(request):
    return render(request, 'pages/contact.html')

def page_info(request):
    return render(request, 'pages/page_info.html')

