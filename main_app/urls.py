from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('findhelp/', views.findhelp, name='findhelp'),
    path('findwork/', views.findwork, name='findwork'),
    path('about/', views.about, name='about'),

]