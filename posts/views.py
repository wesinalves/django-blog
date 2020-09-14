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

def post(request, post_id):
    """Detail page for singular post"""
    post = Post.objects.get(id=post_id)
    comments = post.comment_set.order_by('-date_added')
    context = {'post':post, 'comments':comments}
    return render(request, 'posts/post.html', context)
