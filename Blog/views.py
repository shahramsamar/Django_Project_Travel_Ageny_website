from django.shortcuts import render, get_object_or_404
from Blog.models import Post
from django.utils import timezone




def blog_view(request):
    date_time = timezone.now()
    posts = Post.objects.filter(status=1, published_date__lte=date_time)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)



def blog_single(request, pid):
    date_time = timezone.now()
    post = get_object_or_404(Post, pk=pid, status=1, published_date__lte=date_time)
    related_posts = Post.objects.filter(status=1, published_date__lte=date_time)
    post.counted_views += 1
    post.save()
    context = {'post':post , 'next':related_posts.filter(id__gt=post.id).order_by('id').first(),
               'previous':related_posts.filter(id__lt=post.id).order_by('-id').first() }
    return render(request, 'blog/blog-single.html', context)

def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html', context )
    
    


def test(request):
    return render(request, 'test.html')