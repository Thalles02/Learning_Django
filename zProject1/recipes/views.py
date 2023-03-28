from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def my_viewed(request):
    return HttpResponse("Hello World Urls Django")


def init(request):
    return HttpResponse("Route from init")
