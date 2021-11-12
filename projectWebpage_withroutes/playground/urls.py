from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login', views.login, name='login'),
    path('home', views.home, name='home'),
    path('stock/<str:stockticker>', views.stock, name='stock'),
    path('news', views.news, name='news'),
]