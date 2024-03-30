from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.recipes.factory import make_recipe
from recipes import models

# Create your views here.
def start(request):
    Recipes = models.Recipe.objects.filter(is_publish=True).order_by('-id')

    return render(request, 'recipes/pages/home.html', {
        'recipes' : Recipes,
    })

def recipes(request, id):
    Recipes = models.Recipe.objects.filter(id=id) 

    return render(request, 'recipes/pages/recipe-view.html', {
        'recipe' : Recipes,
        'is_datail_page' : True,
    })

def category(request, category_id):
    # Recipes = models.Recipe.objects.filter(category__id=category_id, is_publish=True).order_by('-id')#Filtrando a através do model Recipe a chave estrangeira através do __ para identificar o id do campo categoria

    Recipes = get_list_or_404(models.Recipe.objects.filter(category__id=category_id, is_publish=True).order_by('-id'))

    return render(request, 'recipes/pages/category.html',
            {
                'recipes' : Recipes,
              #  'title' : f'{Recipes.first().category.name} - Category'    #Seria utilizado se fosse passado uma Queryset
                'title' : f'{Recipes[0].category.name} - Caregory'     #Passando o valor Recipes[0], pois o Recipes é uma Lista
            } 
                  )