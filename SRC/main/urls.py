from django.contrib import admin
from django.urls import path
from main  import views

urlpatterns = [
    path('', views.main_view,name="main"),
    path('home/',views.home_view,name='home')
]