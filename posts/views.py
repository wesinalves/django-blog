from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """The home page for blog"""
    return render(request, 'posts/index.html')

@login_required
def posts(requests):
    """Show all posts."""
    # posts = Post.objects.order_by('date_added')
    # user can view only your own posts
    posts = Post.objects.filter(owner=requests.user).order_by('date_added')
    context = {'posts': posts}
    return render(requests, 'posts/posts.html', context)

@login_required
def post(request, post_id):
    """Detail page for singular post"""
    post = Post.objects.get(id=post_id)
    # make sure the post belongs to the user
    if post.owner != request.user:
        raise Http404
    comments = post.comment_set.order_by('-date_added')
    context = {'post':post, 'comments':comments}
    return render(request, 'posts/post.html', context)

@login_required
def new_post(request):
    """Add a mew post"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = PostForm()
    else:
        # Post data submitted; process data
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('posts:posts'))
    
    context = {'form': form}
    return render(request, 'posts/new_post.html', context)

@login_required
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

@login_required
def edit_comment(request, comment_id):
    """Edit an existing comment."""
    comment = Comment.objects.get(id=comment_id)
    post = comment.post
    if post.owner != request.user:
        raise Http404

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

