'''Define urls for posts'''
from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    # show all posts
    url(r'^posts$', views.posts, name='posts'),

    # Detail page for a single post
    url(r'^posts/(?P<post_id>\d+)/$', views.post, name='post'),

    # add new post
    url(r'^new_post/$', views.new_post, name='new_post'),

    # add new comment
    url(r'^new_comment/(?P<post_id>\d+)/$', views.new_comment, name='new_comment'),
]