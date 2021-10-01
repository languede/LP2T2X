from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
# from django.contrib.auth.models import User
from django.contrib import messages
from authentication.forms import RegistrationForm, LoginForm
from authentication.models import User
# Create your views here.


def reward_home_view(request):
    return render(request, "rewards/index.html")


def login_signup_view(request):
    context = {}
    register_form = RegistrationForm()
    login_form = LoginForm()
    context['registration_form'] = register_form
    context['login_form'] = login_form
    if request.method == "POST":
        if request.POST.get('submit') == 'sign_up':
            register_form = RegistrationForm(request.POST, request.FILES)
            if register_form.is_valid():
                register_form.save()
                user = register_form.cleaned_data.get('username')
                messages.success(request, 'Account was created for' + user)
                return redirect("login-signup")
            else:
                context['registration_form'] = register_form
        if request.POST.get('submit') == 'sign_in':
            phone_number = request.POST.get('username')
            raw_password = request.POST.get('password')
            user = authenticate(request, phone_number=phone_number, password=raw_password)
            if user is not None:
                login(request, user)
                obj = User.objects.get(phone_number=user.phone_number)
                context = {
                    'object': obj
                }
                return user_profile_view(request, context)
            else:
                messages.info(request, 'Phone number OR password is incorrect')
    return render(request, "rewards/login-signup.html", context)


def sign_out(request):
    pass


def user_profile_view(request, user):
    return render(request, "rewards/user_profile.html", user)


def add_green_points_view(request, id):
    context = {}
    if request.method == "POST":
        user = User.objects.get(phone_number=id)
        user.green_point += 10
        user.save()
    return redirect('profile')
    # return render(request, "rewards/user_profile.html", context)
# def user_profile_view(request, *args, **kwargs):
#     return render(request, "rewards/user_profile.html", {})
