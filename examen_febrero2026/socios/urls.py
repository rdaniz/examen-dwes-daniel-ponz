from django.urls import path
from .views import DiscoCreateView, DiscoListView

urlpatterns = [
    path('discos/', DiscoListView.as_view(), name='discos_lista'),
    path('discos/crear/', DiscoCreateView.as_view(), name='disco_crear'),
]
