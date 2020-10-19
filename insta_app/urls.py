from django.urls import path
from .views import ImageListView, ImageDetailView, ImageCreateView, LikeView, ImageUpdateView
from . import views


urlpatterns = [
    path('', ImageListView.as_view(), name='homepage'),
    path('like/<int:pk>', LikeView, name='like_image'),
]
