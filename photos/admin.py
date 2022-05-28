from django.contrib import admin
from .models import Category, Photo, Author, Location

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['category']
    ordering = ['category']
   

admin.site.register(Photo)
admin.site.register(Author)
admin.site.register(Category, ArticleAdmin)
admin.site.register(Location)
