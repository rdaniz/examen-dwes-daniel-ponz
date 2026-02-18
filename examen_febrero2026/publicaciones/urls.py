from django.urls import path
from .views import autores_lista, crear_autor

urlpatterns = [
    path('autores/', autores_lista.as_view(), name='autores_lista'),
    path('autores/crear/', crear_autor.as_view(), name='crear_autor'),
]
