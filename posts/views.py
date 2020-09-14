from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post
from .forms import PostForm

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

def new_post(request):
    """Add a mew post"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = PostForm()
    else:
        # Post data submitted; process data
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('posts:posts'))
    
    context = {'form': form}
    return render(request, 'posts/new_post.html', context)
