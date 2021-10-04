from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()

"""
---------------------
start_page_view: 
---------------------
description:
    start page on self-checkout machine
    if POST & submit request equal to START button: sign user in, authenticate entered value, redirect to shopping_cart
    if authentication fails: display error messages
    if GET: rendering page
"""


def start_page_view(request):
    context = {}
    start_form = StartForm()
    context['start_form'] = start_form
    if request.method == "POST":
        if request.POST.get('submit') == 'HOME':
            return logout_view(request)
        if request.POST.get('submit') == 'LOGOUT':
            return logout_view(request)
        if request.POST.get('submit') == 'START':
            phone_number = request.POST.get('username')
            auth = authenticate(request, phone_number=phone_number)
            if auth is not None:
                login(request, auth)
                user = User.objects.get(phone_number=auth.phone_number)
                context = {
                    'object': user
                }
                return render(request, "shopping_cart.html", context)
            else:
                messages.info(request, 'Phone number OR password is incorrect')
    return render(request, "start_page.html", context)


def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("start_page")


def shopping_cart_view(request):
    """
    TODO: this page should display user_id or username to indicate that user has logged in
          otherwise display a option for registration.
    """
    context = {}
    logout(request)
    register_form = StartForm()
    context['register_form'] = register_form
    return render(request, "shopping_cart.html", context)
