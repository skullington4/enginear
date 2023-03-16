from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('findwork/', views.findwork, name='findwork'),
    path('findjob/', views.findwjob, name='findwork'),
    path('about/', views.about, name='about'),

]