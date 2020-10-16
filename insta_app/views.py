from django.shortcuts import render
from .models import User, Comment


def index(request):
    images = User.objects.all()
    return render(request, 'index.html', {'images': images})
