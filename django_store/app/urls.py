from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    # Category
    path('staff', listCategory),
    path('staff/create-category', CategoryCreateView.as_view()),
    path('staff/update-category/<pk>', CategoryUpdateView.as_view()),
    path('staff/delete-category/<pk>', deleteCategory),


    # Product
    path('staff/list-product', listProduct),
    path('staff/create-product', createProduct),
    path('staff/update-product/<pk>', updateProduct),

    # Order
    path('staff/list-order', listOrder),
    path('staff/view-order/<pk>', viewOrder),

]
