from django.test import TestCase
from .models import Profile, Comment, Post

# Create your tests here.
class PostTestClass(TestCase):
    '''tests for Post(image) class'''
    
    def setUp(self):
                       
        self.post = Post(image = 'name.jpg', imagename='name', caption='caption is a caption', created ='date')        
    
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))  
        
    def test_save_method(self):
        self.post.save()
        post = Post.get_image()
        self.assertTrue(len(post)>0)    
    
class ProfileTestClass(TestCase):
    '''tests for Category'''
    
    def setup(self):
        self.profile = Profile(bio ='this is bio', prophoto ='photo.jpg')    
        
    def test_instance(self):
        self.assertTrue(isinstance(self.Profile))    
        
    def teardown(self):
        Profile.ojects.all().delete
        
    def test_save_method(self):
        self.profile.save()
        profile = Profile.get_post()      
        self.asserTrue(len(profile)>0)  
        
class Comment(TestCase):
    '''tests for Comment'''
    def setup(self):
        self.comment = Comment(text = 'text here', created='date and time')
        
    def teardown(self):
        Comment.objects.all().delete
        
    def test_save_method(self):
        self.comment.save()
        comment=Comment.get_post()
        self.assertTrue(len(comment))
                
        
     
    
    