from calendar import c
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

def loginPage(request):
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
    images= Post.objects.order_by("-created").all()
    
    # current_user = request.user
    user_profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'social/home.html', {'images':images, 'user_profile':user_profile})


@login_required(login_url='login')
def addprofile(request):
    images = Post.objects.all()
    current_user = request.user
    if request.method == 'POST':
        prophoto = request.FILES.get('prophoto')
        # print('data',data)
        # print('prophoto',prophoto)
        profile = Profile.objects.get(user__id=request.user.id)
        profile.bio = request.POST['bio']
        profile.prophoto = prophoto
        profile.save()
        # pro =Profile.objects.get(user__id=request.user.id).update(
        #     bio = data['bio'],
        #     prophoto = prophoto,
        # )
        return redirect ('home')
        
    return render(request, 'social/addprofile.html')

# def updateprofile(request):
    

@login_required(login_url='login')
def profile(request):
    current_user = request.user
    user_profile = get_object_or_404(Profile, user=current_user)
    # user1 = Profile.objects.get(user__id=request.user.id)
    # user_posts = Post.objects.filter(profile=user1)
    # print()

    images = Post.objects.order_by("-created").filter(profile__user=request.user)
    print(images)
    return render(request, 'social/userprofile.html', {'user_profile':user_profile, 'images':images} )

@login_required(login_url='login')
def create_post(request):
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

def viewPhoto(request,pk):
    '''for viewing photo'''
    images = Post.objects.get(id=pk)
    return render(request,'social/photo.html',{'images':images})


def logout_user(request):
    logout(request)
    return redirect('login')





