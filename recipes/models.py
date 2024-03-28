from django.contrib.auth.models import User #importando usuário do próprio Django
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    #definindo método para mudar o nome correto dentro do setor ADMIN do Django
    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=65)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=50)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_publish = models.BooleanField()
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d')
    #quando a categoria for deletada, o campo da receita ficará como NUll
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) #Criando um atributo para fazer a relação da classe Category com a de Recipes
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) #Criando um atributo para fazer a relação da classe Category com a de Recipes

    def __str__(self):
        return self.title
    