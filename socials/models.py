
import profile
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    '''profile model'''
    bio = models.TextField(max_length=255)
    prophoto = models.ImageField(upload_to='profile/',default ='image.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following') 
    followers = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
   
    def __str__(self):
       return self.user.username
   
   
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete =models.CASCADE)
    text = models.TextField(max_length=100) 
    created = models.DateTimeField(auto_now_add=True)
    modified =models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return f'{self.user.username} Post'
    
class Likes(models.Model): 
    count= models.IntegerField()   
    
    def __str__(self):
        return self.count   
   
class Post(models.Model):
     '''image(post) model'''
     
     image = models.ImageField(upload_to='posts/',default='')
     imagename = models.CharField(max_length=20)
     caption = models.TextField(max_length=255)
     profile = models.ForeignKey(Profile, on_delete =models.CASCADE)
     created = models.DateTimeField(auto_now_add=True)
     modified =models.DateTimeField(auto_now=True)
     likes = models.ManyToManyField('Likes', blank=True)
     comments=models.ManyToManyField('Comment', blank=True)
     
     @classmethod
     def get_images(cls):
        images = cls.objects.all()
        return images
   
     def __str__(self):
        return f'{self.profile.user.username} Post'


    


