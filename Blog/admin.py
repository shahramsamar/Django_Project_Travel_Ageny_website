from django.contrib import admin
from Blog.models import Post
# Register your models here.

#@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)