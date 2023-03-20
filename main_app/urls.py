from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('seekhelp/', views.seekhelp, name='seekhelp'),
    path('seekhelp/new/', views.PostCreate.as_view(), name='new'),
    path('seekwork/', views.seekwork, name='seekwork'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
]