from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return render(request, "projects/projects.html")