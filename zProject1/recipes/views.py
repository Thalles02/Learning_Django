from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

name = 'Thalles Augusto Monteiro Martins'


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': Recipe.objects.all(),
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': Recipe.objects.filter(id),
        'is_detail_page': True,
    })
