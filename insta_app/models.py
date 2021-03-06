from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Image(models.Model):
    image = models.ImageField(upload_to='posts/', blank=False)
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField()
    post_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def get_absolute_url(self):
        return reverse('image-detail', kwargs={'pk': self.pk})

    @classmethod
    def search_users(cls, username):
        users = cls.objects.filter(post_creator__icontains=username)
        return users


class Comment(models.Model):
    post = models.ForeignKey(
        Image, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=500, blank=False)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('image-detail', kwargs={'pk': self.post.pk})

    def save_comments(self):
        return self.save()


class Likes(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_likes')
    image_post = models.ForeignKey(
        Image, on_delete=models.CASCADE, related_name='image_post_likes')
