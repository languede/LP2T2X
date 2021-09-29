from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def reward_home(request):
    return render(request, "authentication/index.html")


def login_signup(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['confirm_password']
        image = request.POST['image']
        phone_number = request.POST['phone_number']

        user = User.objects.create_user(username, password, image, phone_number)
        user.save()
        messages.success(request, "Your Account has been successfully created:)")
        return redirect('index')

    return render(request, "authentication/login-signup.html")


def signup(request):
    return render(request, "authentication/login-signup.html")


# def signin(request):
#     return render(request, "reward/signin.html")


def signout(request):
    pass
