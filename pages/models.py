from django.db import models
from django.forms import ImageField
from ckeditor.fields import RichTextField
from datetime import date




class Blog(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    cuerpo = RichTextField(null = True, blank = True)
    autor = models.CharField(max_length=30)
    fecha = models.DateField(default = date.today)
    imagen = models.ImageField(upload_to= 'imagen/', null = True, blank = True)
    
    
    def __str__(self):
        return f'{self.titulo}'
