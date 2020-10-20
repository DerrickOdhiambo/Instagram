# Generated by Django 3.1.2 on 2020-10-20 06:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('insta_app', '0004_auto_20201019_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='image_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
