# Generated by Django 3.1.2 on 2020-10-20 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta_app', '0008_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
