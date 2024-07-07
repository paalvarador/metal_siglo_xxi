from django.contrib import admin
from .models import Product, ProductImage

class ProductImageInline(admin.TabularInline):
    mode = ProductImage

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)
