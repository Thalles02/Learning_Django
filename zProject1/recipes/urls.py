from django.urls import path
from recipes.views import init

urlpatterns = [
    path('inicio', init),
]
