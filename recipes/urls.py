from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'recipes'

urlpatterns = [
    path('', views.start, name='home'),
    path('recipes/<int:id>/', views.recipes, name='recipe'),
]

#servindo os arquivos de imagens para quando serem clicadas, abrirem uma url sem erro
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

