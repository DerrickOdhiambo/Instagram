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
        pass

    def update_caption(self):
        pass

    def get_absolute_url(self):
        return reverse('image--detail', kwargs={'pk': self.pk})

    def delete_image(self):
        pass

    def update_caption(self):
        pass


class Comment(models.Model):
    image = models.ForeignKey(
        'insta_app.Image', related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('homepage')


class Likes(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_likes')
    image_post = models.ForeignKey(
        Image, on_delete=models.CASCADE, related_name='image_post_likes')
