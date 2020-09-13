'''Define urls for posts'''
from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),

    # show all posts
    url(r'^posts$', views.posts, name='posts'),
]