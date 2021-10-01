from django.contrib.auth import authenticate, login
from django.shortcuts import render
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
# def start_page_view(request):
#     return render(request, "start_page.html", {})


def start_page_view(request):
    context = {}
    start_form = StartForm()
    context['start_form'] = start_form
    if request.method == "POST":
        # if request.POST.get('submit') == 'sign_up':
        #     register_form = RegistrationForm(request.POST, request.FILES)
        #     if register_form.is_valid():
        #         register_form.save()
        #         user = register_form.cleaned_data.get('username')
        #         messages.success(request, 'Account was created for' + user)
        #         return redirect("login-signup")
        #     else:
        #         context['registration_form'] = register_form
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
    #  if GET
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
