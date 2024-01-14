from django.shortcuts import render,get_object_or_404
from Blog.models import Post

def blog_view(requests):
    posts = Post.objects.filter(status =1)
    context = {'posts':posts}
    return render(requests,'blog/blog-home.html', context)

def blog_single(requests):
    return render(requests,'blog/blog-single.html')

def test(request, pid):
    # post =Post.objects.get(id=pid)
    post = get_object_or_404(Post, pk= pid)
    context = {'post':post} 
    return render(request,'test.html', context )
