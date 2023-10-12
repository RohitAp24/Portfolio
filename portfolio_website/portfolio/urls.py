from django.urls import path
from . import views

urlpatterns = [  
    path('',views.hhome, name='2.html'),
    path('About', views.About, name='about.html'),
    path('Projects', views.Projects, name='projects.html'),
    path('Home', views.Home, name='2.html'),


]