# Generated by Django 3.1.2 on 2020-10-20 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta_app', '0006_auto_20201020_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]