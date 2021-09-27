from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):  # *args, **kwargs
    print(request.user, args, kwargs)
    return render(request, "home.html", {})  # string of HTML code


def product_detail_view(request, *args, **kwargs):
    return render(request, "product/product_detail.html", {})


def checkout_view(request, *args, **kwargs):
    return render(request, "checkout.html", {})


def about_us_view(request, *args, **kwargs):
    return render(request, "about_us.html", {})


def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})


def start_page_view(request, *args, **kwargs):
    return render(request, "start_page.html", {})


def shopping_cart_view(request, *args, **kwargs):
    return render(request, "shopping_cart.html", {})


def payment_method_view(request, *args, **kwargs):
    return render(request, "payment_method.html", {})
