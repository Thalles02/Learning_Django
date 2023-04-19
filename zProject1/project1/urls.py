from django.contrib import admin
from django.urls import path, include
from recipes.views import *
from django.conf.urls.static import static
# importação do arquivo settings com boas práticas de prog
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('new_routes/', include('recipes.urls')),
    path('', home)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
