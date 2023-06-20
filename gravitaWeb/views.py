from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def projects(request):
    return render(request, "projects.html")

def contactUs(request):
    return render(request, "contact.html")

def clients(request):
    return render(request, "clients.html")
