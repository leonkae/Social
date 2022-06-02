from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def login(request):
    return render(request, 'social/login.html')

def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form':form}
    return render(request, 'social/signup.html', context)