from django.urls import path
from . import views


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('approved/<order_number>', views.approved,
         name='approved'),
    path('cache_checkout_data/', views.cache_checkout_data,
         name='cache_checkout_data'),
   
]