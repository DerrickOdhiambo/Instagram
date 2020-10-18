from django.shortcuts import render
from .models import Image


def index(request):
    images = Image.objects.all()
    return render(request, 'index.html', {'images': images})
