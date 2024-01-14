from django.urls import path
from Blog.views import *

app_name = 'blog'

urlpatterns = [
    # path('urls address,'view',name)
    path('', blog_view, name='index'),
    path('single', blog_single, name="single"),
    path('post-<int:pid>', test, name='test'),
]
