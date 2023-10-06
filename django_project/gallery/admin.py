from django.contrib import admin
from django.utils.safestring import mark_safe

from gallery.models import Gallery, GalleryItem


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_at', 'get_image']
    readonly_fields = ['get_image']
    prepopulated_fields = {'slug': ('name',)}

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="110" height="100"/>')


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_at']
