from django.urls import path
from .views_staff import *

urlpatterns = [
    # path('', index, name='home'),
    # Category
    path('', listCategory, name='home-staff'),
    path('create-category', CategoryCreateView.as_view()),
    path('update-category/<pk>', CategoryUpdateView.as_view()),
    path('delete-category/<pk>', deleteCategory),


    # Product
    path('list-product', listProduct),
    path('create-product', ProductCreateView.as_view()),
    path('update-product/<pk>', ProductUpdateView.as_view()),
    path('delete-product/<pk>', deleteProduct),


    # Order
    path('list-order', listOrder),
    path('view-order/<pk>', viewOrder),
    path('confirm-order-delivered/<pk>', confirmOrderDelivered),
    path('cancel-order/<pk>', cancelOrder),
]
