from django.shortcuts import render
from django.views.generic import ListView , DetailView

from .models import Post

# Create your views here.

class BlogPostsList(ListView):
    template_name = 'home.html'
    model = Post
    context_object_name = 'blogs_list'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'blogs'

