from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from authentication.forms import RegistrationForm
# Create your views here.


def reward_home_view(request):
    return render(request, "rewards/index.html")


def login_signup_view(request):
    context = {}
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            phone_number = form.cleaned_data.get('phone_number')
            raw_password = form.cleaned_data.get('password1')
            username = form.cleaned_data.get('username')
            user = authenticate(phone_number=phone_number, username=username, password=raw_password)
            return redirect("login-signup")
            # login(request, "rewards/index.html", user)
        else:
            context['registration_form'] = form
    else:  # GET
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, "rewards/login-signup.html", context)


def signup(request):
    return render(request, "rewards/login-signup.html")


# def signin(request):
#     return render(request, "reward/signin.html")


def signout(request):
    pass
