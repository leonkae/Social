from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    '''profile model'''
    name = models.CharField(max_length=20, null=False,blank=False)
    username = models.CharField(max_length=20,null=False,blank=False)
    bio = models.CharField(max_length=255)
    profilephoto = models.ImageField(upload_to='media/',default ='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
   
   
    def __str__(self):
       return self.name
   
class Post(models.Model):
     '''image(post) model'''
     image = models.ImageField(upload_to='media/',default='')
     imagename = models.CharField(max_length=20)
     caption = models.CharField(max_length=255)
     user = models.ForeignKey(User, on_delete =models.CASCADE)
     created = models.DateTimeField(auto_now_add=True)
     modified =models.DateTimeField(auto_now_add=True)
     profile =models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
     likes = models.ManyToManyField(User, related_name='likes', blank=True)
   
     def __str__(self):
        return f'{self.user.name} Post'

class Comment(models.Model):
    post =models.ForeignKey(Post, on_delete=models.CASCADE) 
    comment = models.TextField(max_length=100) 
    created = models.DateTimeField(auto_now_add=True)
    modified =models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f'{self.user.name} Post'
    
class Follow(models.Model):
    follow = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following') 
    followers = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')
       

    def __str__(self):
         return f'{self.follow} Follow'

