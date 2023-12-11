from django.shortcuts import render


def blog_view(requests):
    return render(requests,'blog/blog-home.html')

def blog_single(requests):
    return render(requests,'blog/blog-single.html')
