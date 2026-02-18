from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Disco
from .forms import DiscoForm

# Create your views here.

class DiscoListView(ListView):
    model = Disco
    template_name = 'disco_list.html'
    context_object_name = 'discos'

class DiscoCreateView(CreateView):
    model = Disco
    form_class = DiscoForm
    template_name = 'disco_form.html'
    success_url = reverse_lazy('discos_lista')