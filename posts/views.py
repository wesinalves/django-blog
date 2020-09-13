from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    """The home page for blog"""
    return render(request, 'posts/index.html')

def posts(requests):
    """Show all posts."""
    posts = Post.objects.order_by('date_added')
    context = {'posts': posts}
    return render(requests, 'posts/posts.html', context)