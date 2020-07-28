from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='courses'),
    path('<int:course_id>/', views.product_detail, name='course_detail'),
    path('add/', views.add_product, name='add_course'),
    path('edit/<int:course_id>/', views.edit_product, name='edit_course'),
    path('delete/<int:course_id>/', views.delete_product, name='delete_course'),
]
