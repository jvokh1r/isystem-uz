from django.shortcuts import render, redirect
from .models import *


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def courses_view(request):
    posts = Course.objects.filter(is_published=True)
    context = {
        'posts': posts
    }
    return render(request, 'courses.html', context)


