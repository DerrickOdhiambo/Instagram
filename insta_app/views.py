from django.shortcuts import render
from django.views.generic import ListView
from .models import Image


def index(request):
    images = Image.objects.all()
    return render(request, 'index.html', {'images': images})


class ImageListView(ListView):
    model = Image
    template_name = 'index.html'
    context_object_name = 'images'
