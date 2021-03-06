from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):  # *args, **kwargs
    print(request.user, args, kwargs)
    return render(request, "homepage.html", {})  # string of HTML code


def product_detail_view(request, *args, **kwargs):
    return render(request, "product/product_detail.html", {})


def about_us_view(request, *args, **kwargs):
    return render(request, "about_us.html", {})


def introduction_view(request, *args, **kwargs):
    return render(request, "intro.html", {})

