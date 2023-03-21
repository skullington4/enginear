from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('seekhelp/', views.seekhelp, name='seekhelp'),
    path('posts/new/', views.PostCreate.as_view(), name='posts_create'),
    path('posts/<int:pk>/update', views.PostUpdate.as_view(), name='post_update'),
    path('posts/<int:pk>/delete', views.PostDelete.as_view(), name='post_delete'),
    path('posts/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
    path('posts/<int:post_id>/comments/<int:pk>/update', views.CommentUpdate.as_view(), name='comment_update'),
    path('posts/<int:post_id>/comments/<int:pk>/delete', views.CommentDelete.as_view(), name='comment_delete'),
    path('posts/<int:post_id>/', views.post_detail, name='detail'),
    path('seekwork/', views.seekwork, name='seekwork'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    
]