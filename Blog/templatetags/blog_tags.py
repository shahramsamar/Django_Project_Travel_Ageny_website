
from django import template
from Blog.models import Post


register = template.Library()

@register.simple_tag(name='totalposts')
def function():
    post = Post.objects.filter(status=1).count()
    return post


@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts
