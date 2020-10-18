from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    image = models.ImageField(upload_to='posts/', blank=False)
    image_name = models.CharField(max_length=30)
    image_caption = models.TextField()
    post_creator = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField()
    comments = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        pass

    def update_caption(self):
        pass
