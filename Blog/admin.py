from django.contrib import admin
from Blog.models import Post

# @admin.register(Post)


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "create_date"
    empty_value_display = '-empty-'
    list_display = ('title', 'counted_views', 'status',
                    'published_date', 'create_date','author')
    list_filter = ("status",)
    search_fields = ['title', 'content']


admin.site.register(Post, PostAdmin)
