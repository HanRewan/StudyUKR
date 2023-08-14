from django.shortcuts import render
from .models import Course


def allcourses(request):
    courses = Course.objects.all()
    return render(request, 'allcourses.html', {'courses': courses})


def mycourses(request):
    return render(request, 'mycourses.html')