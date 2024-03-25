from django.urls import path
from . import views

urlpatterns = [
    path('', views.start),
    path('recipes/<int:id>/', views.recipes),
]

