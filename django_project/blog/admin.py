from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from blog import models


class RecipeInLine(admin.StackedInline):
    model = models.Recipe
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'create_at', 'id']
    inlines = [RecipeInLine]
    save_as = True
    save_on_top = True


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'prep_time', 'cook_time', 'post']


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'website', 'create_at', 'id']


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Recipe, RecipeAdmin)
admin.site.register(models.Tag)
