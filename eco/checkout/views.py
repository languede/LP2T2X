from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.db.models import F
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned
from .forms import StartForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from products.models import Product, Order
import simplejson as json
from datetime import datetime, timedelta, timezone
import math

User = get_user_model()


class TimeoutException(Exception):
    pass


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
create_order: 
---------------------
description:
    create a new order entry in Table "Order"
"""


def create_order(temp_order, context, user):
    new_order = Order(
        user_id=user.id,
        order_items=json.dumps([temp_order]),
        total_price=temp_order["price"],
        total_point=temp_order["green_point"])
    new_order.save()


"""
---------------------
get_product_view: 
---------------------
description:
    get product data from database Product model
    send product objects as JsonResponse
"""


def get_product_view(request):
    today = datetime.today()
    now_time = datetime.now(timezone.utc)
    barcode_html = request.GET.get("barcode")
    user = request.user
    products = Product.objects.get(barcode=barcode_html)
    green_point = (float(products.price / 7 + 10) * math.e) * products.is_eco
    temp_order = {
        "name": products.name,
        "price": products.price,
        "image": str(products.image),
        "barcode": products.barcode,
        "is_eco": products.is_eco,
        "description": products.description,
        "summary": products.summary,
        "green_point": int(green_point),
    }
    context = [temp_order]
    if not user.is_anonymous:
        try:
            order = Order.objects.filter(user_id=user.id).order_by('-order_date').first()
            time_temp = now_time - order.created_date
            if (time_temp) > timedelta(minutes=15):
                raise TimeoutException()
            else:
                order = Order.objects.filter(user_id=user.id).order_by('-order_date').first()
                order_list = json.loads(order.order_items)
                order_list.append(temp_order)
                order_items = json.dumps(order_list)
                # update field
                order.total_price += products.price
                order.total_point += green_point
                order.order_items = order_items
                order.save()
        except ObjectDoesNotExist:
            create_order(temp_order, context, user)
        except TimeoutException:
            create_order(temp_order, context, user)

    return JsonResponse({"product": context})


def goto_payment_view(request):
    today = datetime.today()
    now_time = datetime.now(timezone.utc)
    user_id = request.user.id
    context = {
        "points": 0,
        "user_points": 0,
        "rating": 0,
    }
    if not request.user.is_anonymous:
        try:
            # update green point in user account
            order = Order.objects.filter(user_id=user_id).order_by('-order_date').first()
            user = User.objects.get(id=user_id)
            user.green_point += order.total_point
            context = {
                "points": order.total_point,
                "user_points": user.green_point,
                "rating": 0,
            }
            user.save()
            return render(request, "celebrate.html", context)
        except ObjectDoesNotExist:
            return HttpResponse('<h1>User Object Not Found</h1>')

    # return redirect("payment_method", context)
    return render(request, "celebrate.html", context)


def payment_method_view(request, *args, **kwargs):
    context = {"object": request.GET}
    return render(request, "payment_method.html", context)

#
# def finish_payment_view(request):
#     return render(request, "finish_payment.html")
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
