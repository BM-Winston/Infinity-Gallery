from django.contrib import admin
from .models import Photos, Category, Location

# Register your models here.

class PhotosAdmin(admin.ModelAdmin):
    filter_horizontal = ('location')

admin.site.register(Category)
admin.site.register(Photos)
admin.site.register(Location)


