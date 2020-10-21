from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Image, Likes, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F


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
    fields = ['image', 'text']

    def form_valid(self, form):
        form.instance.post_creator = self.request.user
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
    success_url = '/'

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
        print(liked)
        Likes.objects.create(user=user, image_post=image_post)
        print('--------------------------------------------')
        print(liked)
        # current_likes = 0
        current_likes = current_likes + 1
        print(current_likes)
        # image_post.likes
        # image_post.save()
    else:
        print(liked)
        Likes.objects.filter(user=user, image_post=image_post).delete()
        print('deletedbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
        # current_likes = current_likes - 1
        # current_likes = 1
        current_likes = current_likes - 1

        print(f'cureeee{current_likes}')
    image_post.likes = current_likes
    image_post.save()

    return HttpResponseRedirect(reverse('image-detail', args=[pk]))
