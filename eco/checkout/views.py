from django.contrib.auth import authenticate, login
from django.shortcuts import render
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
        if request.POST.get('submit') == 'START':
            phone_number = request.POST.get('username')
            user = authenticate(request, phone_number=phone_number)
            if user is not None:
                login(request, user)
                obj = User.objects.get(phone_number=user.phone_number)
                context = {
                    'object': obj
                }
                return render(request, "shopping_cart.html", context)
            else:
                messages.info(request, 'Phone number OR password is incorrect')
    return render(request, "start_page.html", context)

# def product_create_view(request):
#     my_form = ProductForm(request.POST or None)
#     if my_form.is_valid():
#         my_form.save()
#         context = {
#             'form': my_form
#         }
#     return render(request, "product/product_create.html", context)

# def create_user(request):
#     userName = request.REQUEST.get('username', None)
#     userPass = request.REQUEST.get('password', None)
#     userMail = request.REQUEST.get('email', None)
#
#     # TODO: check if already existed
#     if userName and userPass and userMail:
#        u,created = User.objects.get_or_create(userName, userMail)
#        if created:
#           # user was created
#           # set the password here
#        else:
#           # user was retrieved
#     else:
#        # request was empty
#
#     return render(request,'home.html')
