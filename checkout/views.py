from django.shortcuts import render
from .forms import *
from django.contrib.auth.models import User


# Create your views here.
def start_page_view(request):
    return render(request, "start_page.html", {})


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
