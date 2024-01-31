from django.shortcuts import render, get_object_or_404
from Blog.models import Post
from django.utils import timezone



def counted_views(requests, post_id):
    blog_object = Post.objects.get(id=post_id)
    blog_object.counted_views += 1
    blog_object.save()
    return blog_object


def blog_view(requests):
    # date_time = timezone.now()
    # posts = Post.objects.filter(published_date__lte = date_time)
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(requests, 'blog/blog-home.html', context)



def blog_single(requests,pid):
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post}
    return render(requests, 'blog/blog-single.html',context)


def test(request, pid):
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post}
    return render(request, 'test.html', context)
