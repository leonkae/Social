from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
                messages.info(request,'check username or password')
                
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

@login_required(login_url='login')
def home(request):
    return render(request, 'social/home.html')

def logout_user(request):
    logout(request)
    return redirect('login')