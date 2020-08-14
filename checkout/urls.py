from django.conf.urls import url
from .views import checkout


urlpatterns = [
    path('', view.checkout, name='checkout'),
   