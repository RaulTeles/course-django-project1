from django.urls import path
from recipes.views import start

urlpatterns = [
    path('', start),
]

