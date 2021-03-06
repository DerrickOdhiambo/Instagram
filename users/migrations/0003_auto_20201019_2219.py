# Generated by Django 3.1.2 on 2020-10-19 19:19

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201018_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=django_resized.forms.ResizedImageField(crop=None, default='default.jpg', force_format=None, keep_meta=True, quality=75, size=[300, 300], upload_to='profile_pics/'),
        ),
    ]
