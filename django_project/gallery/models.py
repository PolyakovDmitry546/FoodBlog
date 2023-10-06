from django.db import models


class GalleryItem(models.Model):
    """Модель элемента галереи"""

    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='gallery')
    alt = models.CharField(max_length=250, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250)

    def __str__(self) -> str:
        return self.name


class Gallery(models.Model):
    """Модель галереи."""

    name = models.CharField(max_length=250)
    captions = models.CharField(max_length=250, blank=True)
    items = models.ManyToManyField(GalleryItem)
    create_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250)

    def __str__(self) -> str:
        return self.name
