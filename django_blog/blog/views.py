from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm 
from django.contrib.auth import login
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages

# Create your views here.
def RegisterView(request):
    if request.method == 'POST':
         form = RegisterForm(request.POST)
         if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')	
         else:
             messages.error(request, 'Error updating profile') 
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def UserProfile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
        profile.save()

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile) 
        
    return render(request, 'profile.html', {'form': form})