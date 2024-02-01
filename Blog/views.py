from django.shortcuts import render, get_object_or_404
from Blog.models import Post
from django.utils import timezone




def blog_view(requests):
    # date_time = timezone.now()
    # posts = Post.objects.filter(published_date__lte = date_time)
    # view_count = Post.objects.get(id=pid)
    # view_count.counted_views += 1
    # view_count.save()
    posts = Post.objects.filter(status=1)
    # post = get_object_or_404(Post, pk=pid)
    context = {'posts': posts}
    return render(requests, 'blog/blog-home.html', context)



def blog_single(requests, pid):
    date_time = timezone.now()
    date = Post.objects.filter(published_date__lte = date_time)
    
    view_count = Post.objects.get(id=pid)
    view_count.counted_views += 1
    view_count.save()
    
    post = get_object_or_404(Post, pk=pid)
    posts = Post.objects.filter(status=1)
    
    context = {'post': post ,'posts': posts, 'date':date }

    return render(requests, 'blog/blog-single.html', context)


