
from django import template
from django.utils import timezone
from blog.models import Post, Category, Comment


register = template.Library()


@register.simple_tag(name='totalposts')
def function():
    post = Post.objects.filter(status=1).count()
    return post


@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.simple_tag(name='comments_count')
def function(pid):
    post = Post.objects.filter(pk=pid)
    return Comment.objects.filter(post=pid, approved=True).count()



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

@register.inclusion_tag('website/website-latest-post.html')
def latest_post_website():
    date_time = timezone.now()
    posts = Post.objects.filter(status=1, published_date__lte=date_time).order_by('published_date')
    return {'posts': posts }

