from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    '''Post model to the blog'''
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        '''Return a string representation of model'''
        return self.title

class Comment(models.Model):
    '''Comment model for each post'''
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'comments'
    
    def __str__(self):
        '''Return a string representation of model'''
        return self.text[:50] + '...'





