from django.contrib import admin
from django.contrib.admin.filters import ListFilter

from .models import Post, Comment, Category



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'auther', 'status')
    prepopulated_fields = {'slug':('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("status", "published","name" )
    list_filter = ("status", "published", "name")
    search_fields = ("content",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )
    search_fields = ('name', )


    