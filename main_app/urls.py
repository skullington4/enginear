from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('seekinghelp/', views.seekinghelp, name='seekinghelp'),
    path('seekingwork/', views.seekingwork, name='seekingwork'),
    path('about/', views.about, name='about'),

]