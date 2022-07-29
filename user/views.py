from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
            
    else: 
        form = UserRegistrationForm()
    
    return render(request,'registration/sign_up.html', {'form': form})
