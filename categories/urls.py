from django.urls import path
from .views import CategoryCreate, CategoryUpdate, CategoryList, CategoryDetail

urlpatterns = [
    path('categories', CategoryCreate.as_view(), name='product_create'),
    path('categories/<int:pk>', CategoryUpdate.as_view(), name='category_update'),
    path('categories', CategoryList.as_view(), name='category_list'),
    path('categories/<int:pk>', CategoryDetail.as_view(), name='category_detail'),
]