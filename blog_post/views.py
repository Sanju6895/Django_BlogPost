from django.shortcuts import render
from django.views.generic import (ListView, DetailView, 
CreateView, DeleteView, UpdateView)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post


def home(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'blog_post/home.html',context)

def about(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'blog_post/about.html',context)
    #<app>/<model>_<viewname>.html this is what it looks for.

class PostListView(ListView):
    model = Post
    template_name = 'blog_post/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post

#LoginRequiredMixin is similar to login_required decorator
class PostCreateView(LoginRequiredMixin , CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin ,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    #This function allows users to update only their post and not others
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin ,UserPassesTestMixin, DeleteView):
    model = Post
    #success_url is used to redirect user when they delete a post that belongs to them.
    #In this case we redirect to home
    success_url = '/'
     #This function allows users to delete only their post and not others
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False