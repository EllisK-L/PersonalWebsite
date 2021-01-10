from django.shortcuts import render
from django.http import HttpResponse
from home.models import Experience

def home(request):
    experiences = Experience.objects.all()
    return render(request, "home/home.html", {"experiences":experiences})