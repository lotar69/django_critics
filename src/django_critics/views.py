from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1>Bienvenue sur Loic's Critics</h1>")
