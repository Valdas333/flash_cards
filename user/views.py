from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
            
        else: 
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, 'reCaptcha field validation failed!')
                    continue
                messages.error(request, error)
    form = UserRegistrationForm()
    
    return render(request,'registration/sign_up.html', {'form': form})
