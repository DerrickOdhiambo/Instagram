from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    image_path = models.ImageField(upload_to='images/', blank=False)
    insta_story = models.TextField()
    likes = models.IntegerField()

    def __str__(self):
        return self.username


