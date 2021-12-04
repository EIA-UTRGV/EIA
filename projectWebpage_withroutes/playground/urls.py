from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

urlpatterns = [
    path('', views.loginpage, name='landing'),
    path('register', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('accounts/login/', views.loginpage, name='logout'),
    path('home', views.home, name='home'),
    path('stock/<str:stockticker>', views.stock, name='stock'),
    path('news', views.news, name='news'),
]
