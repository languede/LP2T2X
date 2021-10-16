from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned
from .forms import StartForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from products.models import Product, Order
import simplejson as json
from django.template.loader import render_to_string
from datetime import datetime, timedelta, timezone
import math
from orders.views import user_orders
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site

User = get_user_model()

@login_required
def dashboard(request):
    orders = user_orders(request)
    return render(request, 'user/dashboard.html')

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
    new_order_recipe = Order(
        user_id=user.id,
        order_items=json.dumps([temp_order]),
        total_price=temp_order["price"],
        total_point=temp_order["green_point"])
    new_order_recipe.save()


"""
---------------------
create_order: 
---------------------
description:
    add the new added item(dataType=dict) to database "oder_items" column/JsonField 
    update total price and points at sametime
"""


def append_order(order, new_order, price, green_point):
    order_list = json.loads(order.order_items)  # convert order_items json to list[dic1, dic2, etc...]
    order_list.append(new_order)  # append order_items list with new dict(temp_order)
    order_items = json.dumps(order_list)  # convert list back to json
    # update field
    order.total_price += price
    order.total_point += green_point
    order.order_items = order_items
    order.save()


"""
---------------------
get_ordered_item_list: 
---------------------
@input: an Object from Table Order
@return: a list of dict which each dict is a item in shopping cart, 
         for example, order_lists[
                eco_item1{name: eco_item1,..., price: 5}
                eco_item2{name: eco_item2,..., price: 2}
                item1{name: item1,..., price: 500}
                ]
---------------------
description:
    load oder_lists JsonFields in a given entry of database Table Order
    covert the json object to list of dictionaries
    return this list
"""


def get_ordered_item_list(order):
    return json.loads(order.order_items)  # convert order_items json to list[dic1, dic2, etc...]


"""
---------------------
get_product_view: 
---------------------
description:
    get product data from database Product model
    update or add new entry into Table:Order if needed
    return product objects as JsonResponse
"""


def get_product_view(request):
    today = datetime.today()
    now_time = datetime.now(timezone.utc)
    barcode_html = request.GET.get("barcode")
    user = request.user
    products = Product.objects.get(barcode=barcode_html)
    # calculate points, if is_eco == false, green_points = 0
    green_point = int((float(products.price / 3 + 1) * math.e) * products.is_eco)
    temp_order = {
        "name": products.name,
        "price": products.price,
        "image": str(products.image),
        "barcode": products.barcode,
        "is_eco": products.is_eco,
        "description": products.description,
        "summary": products.summary,
        "green_point": green_point,
    }

    if not user.is_anonymous:
        try:
            order = Order.objects.get(user_id=user.id)  # get order by id
            time_temp = now_time - order.created_date
            if time_temp > timedelta(minutes=5):  # if order is edited before 5 minus ago, create new one
                create_order(temp_order, [temp_order], user)
            else:
                append_order(order, temp_order, products.price, green_point)
        except MultipleObjectsReturned:
            order = Order.objects.filter(user_id=user.id).order_by('-order_date').first()
            time_temp = now_time - order.created_date
            if time_temp > timedelta(minutes=5):  # if order is edited before 5 minus ago, create new one
                create_order(temp_order, [temp_order], user)
            else:
                append_order(order, temp_order, products.price, green_point)
        except ObjectDoesNotExist:
            create_order(temp_order, [temp_order], user)
        except TimeoutException:
            create_order(temp_order, [temp_order], user)

    return JsonResponse({"product": [temp_order]})


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

