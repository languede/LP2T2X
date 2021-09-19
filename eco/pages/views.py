from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):  # *args, **kwargs
    print(request.user, args, kwargs)
    return render(request, "home.html", {})  # string of HTML code


def product_detail_view(request, *args, **kwargs):
    return render(request, "details.html", {})


def checkout_view(request, *args, **kwargs):
    return render(request, "checkout.html", {})


def about_us_view(request, *args, **kwargs):
    return render(request, "about_us.html", {})