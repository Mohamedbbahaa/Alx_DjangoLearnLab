from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email', user.email)
        user.save()
        messages.success(request, "Profile updated successfully.")

    return render(request, 'blog/profile.html')

def home(request):
    return render(request, 'blog/base.html')

def posts(request):
    return render(request, 'blog/posts.html')