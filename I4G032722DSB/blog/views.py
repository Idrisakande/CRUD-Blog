from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'Blog/post_list.html'

class PostCreateView(CreateView):
    model = Post
    field = [
        "title"
        "slug"
        "author"
        "body"
        "publish"
        "created"
        "updated"
        "status"
    ]
    template_name = 'Blog/post_list.html'
    success_url  = 'blog/'


class PostDetailView(DetailView):
    model = Post
    template_name = 'Blog/post_detail.html'


class PostUpdateView(UpdateView): 
    model = Post
    field = [
        "title"
        "slug"
        "author"
        "body"
        "publish"
        "created"
        "updated"
        "status"
    ]
    template_name = 'post_up.html'
    success_url  = 'blog/'


class PostDeleteView(DeleteView): 
    model = Post
    fields = [
        "title"
        "slug"
        "author"
        "body"
        "publish"
        "created"
        "updated"
        "status"
    ]  
    template_name = 'Blog/post_confirm_delete.html' 
    success_url  = 'blog/'