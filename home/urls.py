from django.urls import path
from .views import BannerCreate, BannerUpdate, BannerList, BannerDetail, BannerDelete, ContactInfoCreate, ContactInfoUpdate, ContactInfoList, ContactInfoDetail, TestimonialCreate, TestimonialUpdate, TestimonialList, TestimonialDetail, CompanyInfoCreate, CompanyInfoUpdate, CompanyInfoList, CompanyInfoDetail

urlpatterns = [
    path('banners', BannerCreate.as_view(), name='banner_create'),
    path('banners/<int:pk>', BannerUpdate.as_view(), name='banner_update'),
    path('banners', BannerList.as_view(), name='banner_list'),
    path('banners/<int:pk>', BannerDetail.as_view(), name='banner_detail'),
    path('banner/delete/<int:pk>', BannerDelete.as_view(), name='banner_delete'),
]