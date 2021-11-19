from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('home', views.home, name='home'),
    path('stock/<str:stockticker>', views.stock, name='stock'),
    path('news', views.news, name='news'),
]
