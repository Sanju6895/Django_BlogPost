from django.shortcuts import render

# Create your views here.

from .models import Post


def home(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'blog_post/home.html',context)

def about(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'blog_post/about.html',context)
