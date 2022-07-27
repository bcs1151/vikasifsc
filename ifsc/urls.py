from django.contrib import admin
from django.urls import path
from ifsc import views


urlpatterns = [
    path('', views.index, name='home'),
    path('base', views.base, name='base')
]