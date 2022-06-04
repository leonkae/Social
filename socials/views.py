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
                form.save()
                user =form.cleaned_data.get('username')
                messages.success(request, 'Account for' +  user  +  'created succesfully')
                return redirect('login')
                
        context = {'form':form} 
        return render(request, 'social/signup.html', context)

# @login_required(login_url='login')
def home(request):
    images= Post.objects.all()
    return render(request, 'social/home.html', {'images':images})

def addprofile(request):
    images = Post.objects.all()
    current_user = request.user
    if request.method == 'POST':
        data = request.POST
        prophoto = request.FILES.get('prophoto')
        print('data',data)
        print('prophoto',prophoto)
        
        pro =Profile.objects.create(
            bio = data['bio'],
            prophoto = prophoto,
            user = current_user
        )
        pro.save()
        return redirect ('home')
        
    return render(request, 'social/addprofile.html')

def profile(request):
    current_user = request.user
    user_profile = get_object_or_404(Profile, user=current_user)
    return render(request, 'social/userprofile.html', {'user_profile':user_profile} )

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


def logout_user(request):
    logout(request)
    return redirect('login')





