from django.contrib import admin
from django.utils.html import format_html

from .models import Category


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px" />'.format(object.cat_image.url))

    thumbnail.short_description = 'photo'
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('thumbnail', 'category_name', 'slug')


admin.site.register(Category, CategoryAdmin)
