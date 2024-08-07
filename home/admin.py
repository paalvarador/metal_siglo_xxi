from django.contrib import admin
from .models import Banner, CompanyInfo, ContactInfo, Testimonial

class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'image', 'link', 'created_at', 'updated_at']
    search_fields = ['title', 'subtitle', 'link']
    list_filter = ['created_at', 'updated_at']

class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo', 'history', 'mission', 'vision', 'about', 'created_at', 'updated_at']
    search_fields = ['name', 'history', 'mission', 'vision', 'about']
    list_filter = ['created_at', 'updated_at']

class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone', 'email', 'facebook', 'instagram', 'twitter', 'linkedin', 'tiktok', 'created_at', 'updated_at']
    search_fields = ['address', 'phone', 'email', 'facebook', 'instagram', 'twitter', 'linkedin', 'tiktok']
    list_filter = ['created_at', 'updated_at']

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'client_photo', 'testimonial', 'created_at', 'updated_at']
    search_fields = ['client_name', 'testimonial']
    list_filter = ['created_at', 'updated_at']
    
admin.site.register(Banner, BannerAdmin)
admin.site.register(CompanyInfo, CompanyInfoAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
