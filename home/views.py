from rest_framework import generics
from .models import Banner, CompanyInfo, ContactInfo, Testimonial
from .serializer import BannerSerializer, CompanyInfoSerializer, ContactInfoSerializer, TestimonialSerializer

# CRUD BANNER
class BannerCreate(generics.ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class BannerUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class BannerList(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class BannerDetail(generics.RetrieveAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class BannerDelete(generics.DestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

# CRUD COMPANY INFO
class CompanyInfoCreate(generics.ListCreateAPIView):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer

class CompanyInfoUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer

class CompanyInfoList(generics.ListAPIView):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer

class CompanyInfoDetail(generics.RetrieveAPIView):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer

class CompanyInfoDelete(generics.DestroyAPIView):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer

# CRUD CONTACT INFO
class ContactInfoCreate(generics.ListCreateAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer

class ContactInfoUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer

class ContactInfoList(generics.ListAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer

class ContactInfoDetail(generics.RetrieveAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer

class ContactInfoDelete(generics.DestroyAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer

# CRUD TESTIMONIAL
class TestimonialCreate(generics.ListCreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class TestimonialUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class TestimonialList(generics.ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class TestimonialDetail(generics.RetrieveAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class TestimonialDelete(generics.DestroyAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

