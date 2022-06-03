
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    '''profile model'''
    bio = models.CharField(max_length=255)
    profilephoto = models.ImageField(upload_to='media/',default ='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    follow = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following') 
    followers = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
   
    def __str__(self):
       return self.username
   
class Post(models.Model):
     '''image(post) model'''
     image = models.ImageField(upload_to='media/',default='')
     imagename = models.CharField(max_length=20)
     caption = models.CharField(max_length=255)
     user = models.ForeignKey(User, related_name='author', on_delete =models.CASCADE)
     created = models.DateTimeField(auto_now_add=True)
     modified =models.DateTimeField(auto_now=True)
     likes = models.ForeignKey(User, on_delete=models.CASCADE,related_name='likes', blank=True)
     comments=models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
     
     
   
     def __str__(self):
        return f'{self.user.username} Post'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete =models.CASCADE)
    post =models.ForeignKey(Post, on_delete=models.CASCADE) 
    comment = models.TextField(max_length=100) 
    created = models.DateTimeField(auto_now_add=True)
    modified =models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return f'{self.user.username} Post'
    


