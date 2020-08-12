from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add/<course_id>/', views.add_to_basket, name='add_to_basket'),
    path('delete/<course_id>/', views.delete_from_basket, name='delete_from_basket'),
]
