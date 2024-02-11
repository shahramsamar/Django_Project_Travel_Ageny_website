from django.shortcuts import render, get_object_or_404
from Blog.models import Post
from django.utils import timezone




def blog_view(requests):
    date_time = timezone.now()
    posts = Post.objects.filter(status=1,published_date__lte=date_time)
    context = {'posts': posts}
    return render(requests, 'blog/blog-home.html', context)



def blog_single(requests, pid):
    date_time = timezone.now()
    post = get_object_or_404(Post, pk=pid, status=1, published_date__lte=date_time)
    # current_posts =Post.objects.get(pk =pid)
    related_posts = Post.objects.all()
    post.counted_views += 1
    post.save()
    context = {'post':post , 'next':related_posts.filter(id__gt=post.id).order_by('id').first(),
               'previous':related_posts.filter(id__lt=post.id).order_by('-id').first() }
    return render(requests, 'blog/blog-single.html', context)


