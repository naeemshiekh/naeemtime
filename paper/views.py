from django.shortcuts import render
from .models import Post, Journalist
from django.views.generic import ListView 

# Create your views here.
class NewsListView(ListView):
    model = Post
    template_name = 'main/base.html'
    context_object_name = 'posts'  # Use a different context name to avoid conflicts