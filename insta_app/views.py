from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Image
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    images = Image.objects.all()
    return render(request, 'index.html', {'images': images})


class ImageListView(ListView):
    model = Image
    template_name = 'index.html'
    context_object_name = 'images'


def LikeView(request, pk):
    image_post = get_object_or_404(Image, id=request.POST.get('image_id'))
    image_post.likes.add(request.user)
    return HttpResponseRedirect(reverse('image-detail', args=[str(pk)]))
