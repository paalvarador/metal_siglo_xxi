from django.urls import path
from .views import BannerCreate, BannerUpdate, BannerList, BannerDetail, BannerDelete, ContactInfoCreate, ContactInfoUpdate, ContactInfoList, ContactInfoDetail, TestimonialCreate, TestimonialUpdate, TestimonialList, TestimonialDetail, CompanyInfoCreate, CompanyInfoUpdate, CompanyInfoList, CompanyInfoDetail

urlpatterns = [
    path('home', BannerCreate.as_view(), name='banner_create'),
    path('home/<int:pk>', BannerUpdate.as_view(), name='banner_update'),
    path('home', BannerList.as_view(), name='banner_list'),
    path('home/<int:pk>', BannerDetail.as_view(), name='banner_detail'),
    path('home/delete/<int:pk>', BannerDelete.as_view(), name='banner_delete'),
]