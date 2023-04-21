from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

name = 'Thalles Augusto Monteiro Martins'


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id, is_published=True).order_by('-id')

    if not recipes:
        # Return render com a page 404 e passa o statuscode como parametro
        return HttpResponse(content='Not Found', status=404)

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes.first().category.name} - Category |'
    })


def recipe(request, id):
    recipe = Recipe.objects.filter(
        id=id, is_published=True).order_by('-id').first()

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })
