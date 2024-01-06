from django.contrib import admin
from Blog.models import Post
# Register your models here.

#@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
   date_hierarchy = "create_date"
   #empty_value_display = '-empty-'
   list_display =('title', 'counted_views', 'status', 'published', 'create_date',)
   list_filter =("status",)
   ordering =['-create_date']
   search_fields =['title','content']
   
admin.site.register(Post, PostAdmin)