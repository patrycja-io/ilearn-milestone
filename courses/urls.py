from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_courses, name='courses'),
    path('<int:course_id>/', views.course_description,
         name='course_description'),
    path('add/', views.add_course, name='add_course'),
    path('edit/<int:course_id>/', views.edit, name='edit'),
    path('delete/<int:course_id>/', views.delete_course, name='delete_course'),
]
