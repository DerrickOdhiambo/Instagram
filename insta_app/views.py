from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Image, Likes, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import CommentForm
from django.contrib.auth.models import User


def index(request, id):
    images = Image.objects.all()
    return render(request, 'index.html', {'images': images})


class ImageListView(ListView):
    model = Image
    template_name = 'index.html'
    context_object_name = 'images'


class ImageDetailView(DetailView):
    model = Image


class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Image
    fields = ['image', 'image_caption']

    def form_valid(self, form):
        form.instance.post_creator = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Image.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)


class ImageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Image
    fields = ['image', 'image_caption']

    def form_valid(self, form):
        form.instance.post_creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        image_post = self.get_object()
        if self.request.user == image_post.post_creator:
            return True
        return False


class ImageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Image
    success_url = reverse_lazy('homepage')

    def test_func(self):
        image_post = self.get_object()
        if self.request.user == image_post.post_creator:
            return True
        return False


def LikeView(request, pk):
    user = request.user
    image_post = Image.objects.get(id=pk)
    current_likes = image_post.likes

    liked = Likes.objects.filter(user=user, image_post=image_post)
    # print(liked)
    if not liked:
        Likes.objects.create(user=user, image_post=image_post)
        current_likes = current_likes + 1

    else:
        Likes.objects.filter(user=user, image_post=image_post).delete()
        current_likes = current_likes - 1

    image_post.likes = current_likes
    image_post.save()

    return HttpResponseRedirect(reverse('image-detail', args=[pk]))


def search(request):
    return render(request, 'search.html')


class SearchListView(ListView):
    model = User
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['query'] = self.request.GET.get('q')
        context['posts'] = Image.objects.filter(image_caption__icontains=query)
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = User.objects.filter(username__icontains=query)
        return object_list
