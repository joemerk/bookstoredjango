#adapted from https://github.com/guinslym/django-by-example-book
from django.contrib import admin
from .models import Headphone, Manufacturer, ModelNo

class ModelNoAdmin(admin.ModelAdmin):
    list_display = ['modelno', 'slug']
    prepopulated_fields = {'slug': ('modelno',)}
admin.site.register(ModelNo, ModelNoAdmin)


class HeadphoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'manufacturers', 'modelno', 'price', 'stock', 'available', 'release_date']
    list_filter = ['available', 'release_date', 'modelno']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Headphone, HeadphoneAdmin)

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['manufacturer_name', 'slug']
    prepopulated_fields = {'slug': ('manufacturer_name',)}
admin.site.register(Manufacturer, ManufacturerAdmin)
