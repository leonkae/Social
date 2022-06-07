from ast import keyword
from django.shortcuts import get_object_or_404, render,redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def loginPage(request):
    '''login view'''
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            print(username,password,user)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request,'Check username or password !')
                
        return render(request, 'social/login.html')

def signup(request):
    '''signup view'''
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                username =form.cleaned_data.get('username')
                created_user = form.save()
                Profile.objects.get_or_create(user=created_user)
                messages.success(request, 'Account for' +  username  +  'created succesfully')
                return redirect('login')
                
        context = {'form':form} 
        return render(request, 'social/signup.html', context)

@login_required(login_url='login')
def home(request):
    '''home view'''
    images= Post.objects.order_by("-created").all()
    user_profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'social/home.html', {'images':images, 'user_profile':user_profile})


@login_required(login_url='login')
def addprofile(request):
    '''add profile view'''
    images = Post.objects.all()
    current_user = request.user
    if request.method == 'POST':
        prophoto = request.FILES.get('prophoto')
        profile = Profile.objects.get(user__id=request.user.id)
        profile.bio = request.POST['bio']
        profile.prophoto = prophoto
        profile.save()
        return redirect ('home')
        
    return render(request, 'social/addprofile.html')
    

@login_required(login_url='login')
def profile(request):
    '''profile view'''
    
    current_user = request.user
    user_profile = get_object_or_404(Profile, user=current_user)
    images = Post.objects.order_by("-created").filter(profile__user=request.user)
    image_length = (len(images))
    return render(request, 'social/userprofile.html', {'user_profile':user_profile, 'images':images, 'image_length':image_length} )

@login_required(login_url='login')
def create_post(request):
    '''create post view'''
    images = Post.objects.all()
    current_user = request.user
    user_profile = get_object_or_404(Profile, user=current_user)
    
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        print('data', data)
        print('image', image)
        
        post = Post.objects.create(   
            caption = data['caption'],
            imagename = data['imagename'],
            image =image,
            profile=user_profile,
        )
        post.save()
        return redirect('home')
    
    return render(request, 'social/create.html' )

def LikeView(request,pk):
    '''like view'''
    if request.method =='POST':
        post = get_object_or_404(Post, id=pk)
        post.likes.add(request.user)
        print(post)
    
        return HttpResponseRedirect(reverse('home'))
    return redirect('home')


@login_required(login_url='login')    
def Comment(request):
    '''comment view'''
    current_user = request.user
    user_profile = get_object_or_404(Profile, user=current_user)
    
    if request == 'POST':
        data=request.POST
        comment =request.FILES.get('comment')
        print('data',data)
        print('comment',comment)
        
    return render(request, 'social/comment.html')     

def viewPhoto(request,pk):
    '''viewphoto view'''
    images = Post.objects.get(id=pk)
    return render(request,'social/photo.html',{'images':images})


def logout_user(request):
    '''logout view '''
    logout(request)
    return redirect('login')





