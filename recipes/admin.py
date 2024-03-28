from django.contrib import admin
from . import models

class CategoryAdmin(admin.ModelAdmin):
    ...

admin.site.register(models.Category, CategoryAdmin)#Primeira forma de registrar um modelo na pagina admin


@admin.register(models.Recipe)#segunda forma de registrar um modelo na pagina admin
class RecipeAdmin(admin.ModelAdmin):
    ...
