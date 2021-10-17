from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.models import User
from django.contrib import messages
from authentication.forms import RegistrationForm, LoginForm
from authentication.models import User
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm
from products.models import Order

from django.db.models import Sum
from django.db.models import Count

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import CustomPasswordChangeForm


# homepage
def reward_home_view(request):
    return render(request, "index.html")


"""
---------------------
login_signup_view: 
---------------------
description:
    login and signup page
    if POST & sign up button has been clicked => save form into database and redirect to profile page.
    if GET => Rendering webpage with LoginForm and RegistrationForm
"""


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
            return redirect('store:all_products')
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

    context = {'page': page, 'form': form}
    return render(request, 'index.html', context)


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
    reset_password_form = CustomPasswordChangeForm(request.user)
    # orders = user_info.order_set.all()
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).order_by('order_date')

    if request.method == 'POST':
        # Update user information
        if request.POST.get('submit') == 'Update':
            form = ProfileForm(request.POST, request.FILES, instance=user_info)
            if form.is_valid():
                form.save()
                return redirect('profile')

        elif request.POST.get('submit') == 'Reset Password':
            reset_password_form = CustomPasswordChangeForm(request.user, request.POST)
            if reset_password_form.is_valid():
                user = reset_password_form.save()
                update_session_auth_hash(request, user)
                return redirect('profile')
            else:
                messages.error(request, 'Failed to reset password')

    context = {'form': form, 'orders': orders, 'reset_form': reset_password_form, }
    return render(request, 'user_profile.html', context)


# eco-rating page
@login_required(login_url='login')
def eco_rating_view(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).all()

    # the point for the last purchase
    last_order = Order.objects.filter(user_id=user_id).order_by('order_date').last()
    if last_order is not None:
        last_order_point = last_order.total_point
    else:
        last_order_point = 0

    if not request.user.is_authenticated:
        messages.error(request, 'Please sign in to Eco Rewards')
        return redirect('reward_home')
    else:
        points_sum = orders.aggregate(nums=Sum('total_point'))
        orders_num = orders.aggregate(nums=Count('created_date'))
        num = orders_num['nums']
        if num == 0:
            avg_points = 0
            points_sum['nums'] = 0
        else:
            avg_points = int(points_sum['nums'] / num)
        context = {'points': request.user.green_point, 'avg_points': avg_points, 'last_order_point': last_order_point}

    return render(request, "user-eco.html", context)
