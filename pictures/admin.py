from django.contrib import admin
from .models import Category, Post, Author
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['category']
    ordering = ['category']
    search_fields = ['category']

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Category, ArticleAdmin)
