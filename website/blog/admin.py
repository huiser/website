from django.contrib import admin
from blog.models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'public', 'description',)
    list_display = ('name', 'public', 'description', )
    list_display_links = ('name',)
    list_filter = ('public',)
    ordering = ('name', )
    search = ('name', 'description', )

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'category', 'author', 'state', 'published_at', 'body', 'tags', )
    list_display = ('title', 'author', 'category', 'state', 'published_at', )
    list_display_links = ('title', )
    list_filter = ('author', 'state', 'category',)
    ordering = ('published_at', )
    search = ('title',)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
