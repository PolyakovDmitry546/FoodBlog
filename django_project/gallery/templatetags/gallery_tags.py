from django import template

from gallery.models import GalleryItem

register = template.Library()


@register.inclusion_tag('gallery/include/tags/gallery_tag.html')
def get_gallery():
    gallery_items = GalleryItem.objects.order_by()[:5]
    return {'gallery_items': gallery_items}
