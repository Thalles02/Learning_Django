from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

name = 'Thalles Augusto Monteiro Martins'


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': name,
    })


def init(request):
    return HttpResponse("Route from init")
