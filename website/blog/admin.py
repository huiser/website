from django.contrib import admin
from blog.models import Category

class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'public', 'description',)
    list_display = ('name', 'public', 'description', )
    list_display_links = ('name',)
    list_filter = ('public',)
    ordering = ('name', )
    search = ('name', 'description', )


admin.site.register(Category, CategoryAdmin)
