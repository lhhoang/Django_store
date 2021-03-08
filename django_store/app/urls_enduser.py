from django.urls import path
from .views_enduser import *

urlpatterns = [
    path('', index),
    path('view-product/<pk>', viewProduct),
    path('order-product/<pk>', orderProduct),
    path('thank-you', thankYou),
]
