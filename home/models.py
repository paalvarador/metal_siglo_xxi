from django.db import models

# Model to manage de Sliders show in the HomePage (Swiper)
class Banner(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='banners/')
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    tiktok = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address

class Testimonial(models.Model):
    client_name = models.CharField(max_length=255)
    client_photo = models.ImageField(upload_to='client_photos/', blank=True, null=True)
    testimonial = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name

class CompanyInfo(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='company_logo/', blank=True, null=True)
    history = models.TextField()
    mission = models.TextField()
    vision = models.TextField()
    about = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name


