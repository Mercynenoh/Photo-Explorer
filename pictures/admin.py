from django.contrib import admin
from .models import Category, Post, Author, Location
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['category']
    ordering = ['category']
    search_fields = ['foreignkeyfield__name']

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Location)
admin.site.register(Category, ArticleAdmin)
