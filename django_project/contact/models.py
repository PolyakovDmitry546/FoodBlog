from django.db import models
from ckeditor.fields import RichTextField


class ContactModel(models.Model):
    """ Класс модели обратной связи """

    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f'{self.name} - {self.email}'
    

class ContactLink(models.Model):
    """Класс модели контактов"""

    icon = models.FileField(upload_to='icons/')
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name



class About(models.Model):
    """Класс модели страницы о нас"""

    text = RichTextField()
    mini_text = RichTextField()

    def get_first_image(self):
        return self.about_images.first()
    
    def get_images(self):
        return self.about_images.all()[1:]


class AboutImage(models.Model):
    """Класс модели изображений страницы о нас"""

    image = models.ImageField(upload_to='about/')
    page = models.ForeignKey(About, on_delete=models.CASCADE, related_name='about_images')
    alt = models.CharField(max_length=100, default='')


class Social(models.Model):
    """Класс модели социальных сетей страницы о нас"""

    icon = models.FileField(upload_to='icons/')
    name = models.CharField(max_length=200)
    link = models.URLField()