from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SignUpForm
from django.contrib.auth import logout, login
from django.conf import settings


def signupView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
        return render(request, "registration/sign-up.html", {"form": form})
        
    else:
        form = SignUpForm()
        return render(request, "registration/sign-up.html", {"form": form})


def logoutView(request):
    logout(request)
    return redirect(reverse('home'))