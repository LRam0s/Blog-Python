from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView,DeleteView
from pages.models import Blog

# Create your views here.

class PagesList(ListView):
    model = Blog
    template_name = 'pages/list_pages.html'

class DetailPages(DetailView):
    model = Blog
    template_name = 'pages/detail_pages.html'

class CreatePages(CreateView):
    model = Blog
    success_url = '/pages/'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha', 'imagen']

class EditPages(UpdateView):
    model = Blog
    success_url = '/pages/'
    
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha', 'imagen']

class DeletePages(DeleteView):
    model = Blog
    success_url = '/pages/'
    