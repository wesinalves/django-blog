from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post, Comment
from .forms import PostForm, CommentForm

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

def new_comment(request, post_id):
    """Add a mew comment"""
    post = Post.objects.get(id=post_id)

    if request.method != 'POST':
        # No data submitted; create a blank form
        form = CommentForm()
    else:
        # Comment data submitted; process data
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse('posts:post', args=[post_id]))
    
    context = {'post':post, 'form': form}
    return render(request, 'posts/new_comment.html', context)

def edit_comment(request, comment_id):
    """Edit an existing comment."""
    comment = Comment.objects.get(id=comment_id)
    post = comment.post

    if request.method != 'POST':
        # Initial request; pre-fill form with the current commentary. 
        form = CommentForm(instance=comment)
    else:
        # POST data submitted; process data.
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('posts:post', args=[post.id]))
    
    context = {'comment': comment, 'post': post, 'form': form}
    return render(request, 'posts/edit_comment.html', context)

