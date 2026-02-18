from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Autor
from .forms import AutorForm

# Create your views here.
class autores_lista(ListView):
    model = Autor
    template_name = 'autor_list.html'
    context_object_name = 'autores'

class crear_autor(CreateView):
    model = Autor
    form_class = AutorForm   
    template_name = 'publicaciones/autor_form.html'
    success_url = '/autores/'