from django.urls import path
from .views import ImageListView, LikeView, ImageUpdateView, ImageDetailView, ImageCreateView, ImageDeleteView, CommentCreateView
from . import views


urlpatterns = [
    path('', ImageListView.as_view(), name='homepage'),
    path('post/<int:pk>/', ImageDetailView.as_view(), name='image-detail'),
    path('post/new/', ImageCreateView.as_view(), name='image-create'),
    path('post/<int:pk>/update/', ImageUpdateView.as_view(), name='image-update'),
    path('post/<int:pk>/delete/', ImageDeleteView.as_view(), name='image-delete'),
    path('post/<int:pk>/comment/',
         CommentCreateView.as_view(), name='comment-create'),
    path('post/<int:pk>/like/', LikeView, name='like_image'),
]
