
from django import template
from Blog.models import Post, Category


register = template.Library()


@register.simple_tag(name='totalposts')
def function():
    post = Post.objects.filter(status=1).count()
    return post


@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts


@register.filter
def snippet(value, arg=20):
    return value[:arg] + "..."


@register.inclusion_tag('blog/blog-latest-post.html')
def latest_posts():
    post = Post.objects.filter(status=1).order_by('published_date')[:3]
    return {'post': post}


@register.inclusion_tag('blog/blog-post-category.html')
def post_category():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories': cat_dict}
