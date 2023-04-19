from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)  # registrando model no admin da segunda maneira
class RecipeAdmin(admin.ModelAdmin):
    ...


# registrando model no admin 1° maneira
admin.site.register(Category, CategoryAdmin)
