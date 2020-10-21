# Generated by Django 3.1.2 on 2020-10-20 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('insta_app', '0005_auto_20201020_0921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='image',
            name='likes',
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_post_likes', to='insta_app.image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]