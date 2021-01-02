from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('payment_approved/<order_number>', views.payment_approved, 
         name='checkout_success'),
    path('cache_data/', views.cache_data, name='cache_data'),
    path('wh/', webhook, name='webhook'),
]


