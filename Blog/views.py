from django.shortcuts import render, get_object_or_404
from Blog.models import Post
from django.utils import timezone




def blog_view(requests):
    date_time = timezone.now()
    posts = Post.objects.filter(status=1) & Post.objects.filter(published_date__lte=date_time)
    # post = get_object_or_404(Post, pk=pid)
    context = {'posts': posts}
    return render(requests, 'blog/blog-home.html', context)



def blog_single(requests, pid):
    view_count = Post.objects.get(id=pid)
    view_count.counted_views += 1
    view_count.save()
    date_time = timezone.now()
    post = get_object_or_404(Post, pk=pid) or Post.objects.filter(status=1 ) & Post.objects.filter(published_date__lte=date_time)
    context = {'post':post }
    return render(requests, 'blog/blog-single.html', context)


