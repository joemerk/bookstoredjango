#adapted from https://github.com/guinslym/django-by-example-book
from django.contrib import admin
from .models import Headphone, Manufacturer, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'slug']
    prepopulated_fields = {'slug': ('category',)}
admin.site.register(Category, CategoryAdmin)


class HeadphoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'manufacturers', 'category', 'price', 'stock', 'available', 'release_date']
    list_filter = ['available', 'release_date', 'category']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Headphone, HeadphoneAdmin)

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['manufacturer_name', 'slug']
    prepopulated_fields = {'slug': ('manufacturer_name',)}
admin.site.register(Manufacturer, ManufacturerAdmin)
