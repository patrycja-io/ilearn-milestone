from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
     path('payment_approved/<order_number>', views.payment_approved, name='payment_approved'),
]

