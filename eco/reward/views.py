from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.models import User
from django.contrib import messages
from authentication.forms import RegistrationForm, LoginForm
from authentication.models import User
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm
from .forms import ResetPasswordForm
from .models import Order

from django.db.models import Sum


# homepage
def reward_home_view(request):
    return render(request, "index.html")


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == "POST":
        phone = request.POST['phone']
        password = request.POST['password']

        try:
            user = User.objects.get(phone_number=phone)
        except:
            messages.error(request, "Username does not exist")

        user = authenticate(request, phone_number=phone, password=password)

        if user is not None:
            login(request, user)
            return redirect('reward_home')
        else:
            messages.error(request, 'Username OR password is incorrect')
        
    return render(request, 'index.html')


def registerUser(request):
    page = 'register'
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('reward_home')

        else:
            messages.error(request, 'Error occurred')

    context = {'page': page, 'form':form}
    return render(request, 'index.html', context)


"""
---------------------
login_signup_view: 
---------------------
description:
    login and signup page
    if POST & sign up button has been clicked => save form into database and redirect to profile page.
    if GET => Rendering webpage with LoginForm and RegistrationForm
"""


# def login_signup_view(request):
#     context = {}
#     register_form = RegistrationForm()
#     login_form = LoginForm()
#     context['registration_form'] = register_form
#     context['login_form'] = login_form
#     if request.method == "POST":
#         if request.POST.get('submit') == 'sign_up':
#             register_form = RegistrationForm(request.POST, request.FILES)
#             if register_form.is_valid():
#                 register_form.save()
#                 user = register_form.cleaned_data.get('username')
#                 messages.success(request, 'Account was created for' + user)
#                 return redirect("login-signup")
#             else:
#                 context['registration_form'] = register_form
#         else:
#             phone_number = request.POST.get('username')
#             raw_password = request.POST.get('password')
#             user = authenticate(request, phone_number=phone_number, password=raw_password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('profile')
#             else:
#                 messages.info(request, 'Phone number OR password is incorrect')
#     return render(request, "login-signup.html", context)


"""
---------------------
sign_out: 
---------------------
description:
    sign user out
    there should be a button to allowed sign out actions
"""


def logoutUser(request):
    logout(request)
    return redirect('reward_home')


"""
---------------------
user_profile_view: 
---------------------
description:
    user profile page
    if POST & submit request equal to add_points => update user's current green point in database
    if POST & submit request equal to sign_in => sign user in, authenticate form and refresh profile page
"""

@login_required(login_url='login')
def user_profile_view(request):
    user_info = request.user
    form = ProfileForm(instance=user_info)
    reset_password_form = ResetPasswordForm(instance=user_info)
    orders = user_info.order_set.all()

    if request.method == 'POST':
        # Update user information
        if request.POST.get('submit') == 'Update':
            form = ProfileForm(request.POST, request.FILES, instance=user_info)
            if form.is_valid():
                form.save()
                return redirect('profile')

        elif request.POST.get('submit') == 'Reset Password':
            reset_password_form = ResetPasswordForm(request.POST, request.FILES, instance=user_info)
            if form.is_valid():
                form.save()
                return redirect('profile')

    context = {'form': form, 'orders': orders, 'reset_form': reset_password_form}
    return render(request, 'user_profile.html', context)


@login_required(login_url='login')
def reset_password_view(request):
    user_info = request.user
    form = ResetPasswordForm(instance=user_info)

    if request.method == 'POST':
        if request.POST.get('submit') == 'Reset Password':
            form = ResetPasswordForm(request.POST, request.FILES, instance=user_info)
            if form.is_valid():
                form.save()
                return redirect('profile')
    
    context = {'form': form,}
    return render(request, 'user_profile.html', context)

#eco-rating page
# @login_required(login_url='login')
def eco_rating_view(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Please sign in to Eco Rewards')
        return redirect('reward_home')
    else:
        points = Order.objects.filter(user=request.user).all()
        points_sum = points.aggregate(nums=Sum('points'))

        context = {'points': points_sum['nums']}

    return render(request, "user-eco.html", context)