from django.shortcuts import render
from myapp.models import Image, Board, Pin
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse
from .forms import ModelFormWithFileField

class ImageCreateView(CreateView):
    model = Image
    template_name = 'image_create.html'
    fields = ['image']
    def get_success_url(self):
        return reverse('home')

class ImageListView(ListView):
    model = Image
    #queryset=Student.objects.filter(type='mountain')
    template_name = 'image_list.html'