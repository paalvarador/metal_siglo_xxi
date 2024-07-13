from django.urls import path
from .views import ProductCreate, ProductUpdate, ProductList, ProductDetail

urlpatterns = [
    path('products', ProductCreate.as_view(), name='product_create'),
    path('products/<int:pk>', ProductUpdate.as_view(), name='product_update'),
    path('products', ProductList.as_view(), name='product_list'),
    path('products/<int:pk>', ProductDetail.as_view(), name='product_detail'),
]