from django.contrib import admin
from django.urls import path, include
from recipes.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('new_routes/', include('recipes.urls')),
    path('', home)
]
