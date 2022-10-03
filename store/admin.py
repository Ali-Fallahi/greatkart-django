from django.contrib import admin
from django.utils.html import format_html

from .models import Product


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px" />'.format(object.images.url))

    thumbnail.short_description = 'photo'
    list_display = ('thumbnail', 'product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}


admin.site.register(Product, ProductAdmin)
