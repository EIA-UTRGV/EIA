from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home', views.home, name='home'),
    path('stock/<str:stockticker>', views.stock, name='stock'),
    path('news', views.news, name='news'),
]