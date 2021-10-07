from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from .forms import StartForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from products.models import Product

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
    context['flag'] = True
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


"""
---------------------
logout_view: 
---------------------
description:
    view for logout button, ensure user has logged out
    then redirect to shopping cart page 
"""


def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("start_page")


"""
---------------------
shopping_cart_view: 
---------------------
description:
    view for back to home button, ensure user has logged out
    then redirect to shopping cart page 
"""


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


"""
---------------------
get_product_view: 
---------------------
description:
    get product data from database Product model
    send product objects as JsonResponse
"""


# def get_product_view(request):
#     products = Product.objects.all()
#     temp = list(products.values())
#     return JsonResponse({"product": list(products.values())})

def get_product_view(request):
    barcode_html = request.GET.get("barcode")
    products = Product.objects.get(barcode=barcode_html)
    green_point = products.price * products.is_eco
    temp = {
        "name": products.name,
        "price": products.price,
        "image": str(products.image),
        "barcode": products.barcode,
        "is_eco": products.is_eco,
        "description": products.description,
        "summary": products.summary,
        "green": green_point,
    }
    context = [temp]
    return JsonResponse({"product": context})


def payment_method_view(request, *args, **kwargs):
    return render(request, "payment_method.html", {})


# def get(request):
#     barcode = request.GET.get("barcode")
#     msg = {"status": 200, "result": None}
#     try:
#         goods_obj = Product.objects.get(barcode=barcode)
#         goods_info = {
#             "barcode": goods_obj.barcode,
#             "price": goods_obj.price,
#             "img": f"media/{goods_obj.img}",
#         }
#         msg["result"] = goods_info
#         return JsonResponse(msg)
#     except:
#         msg["status"] = 400
#         msg["result"] = "Request error, please check whether the barcode is correct."
#
#         return JsonResponse(msg)
