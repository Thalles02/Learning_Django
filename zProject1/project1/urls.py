from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def my_viewed(request):
    return HttpResponse("Hello World Urls Django")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sobre/', my_viewed),
]
