from django.contrib import admin
from .models import BlogPost, SubCategory

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'subcategory', 'published_date')
    list_filter = ('subcategory', 'published_date')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(SubCategory)
