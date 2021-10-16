import json

import stripe
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

import payment.views
from basket.basket import Basket
from django.contrib.auth import get_user_model

User = get_user_model()


def order_placed(request):
    basket = Basket(request)
    basket.clear()
    return render(request, 'payment/orderplaced.html')


class Error(TemplateView):
    template_name = 'payment/error.html'


# before payment user be required login
@login_required(login_url='login')
def payByGreenView(request):
    basket = Basket(request)
    total_point_cost = int(basket.get_total_greenpoint())
    user = User.objects.get(id=request.user.id)
    check_user_points_changes = user.green_point - total_point_cost
    if check_user_points_changes < 0:
        # no enough points to purchase
        context = {"no_points": True, "green_points": user.green_point}
        return render(request, 'basket/summary.html', context)
    elif check_user_points_changes >= 0:
        user.green_point -= total_point_cost
        user.save()
        context = {"no_points": False}
        basket.clear()

    return render(request, 'payment/orderplaced.html', context)


# before payment user be required login
@login_required(login_url='login')
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_greenpoint())
    total = total.replace('.', '')
    total = int(total)

    stripe.api_key = 'sk_test_51JjiBRDJaj9YScNg80KFVH0YXrbzvnoSR4jB0KgmoIyAd34Aa5dZ7i1BKko1IUE7vtAYYzYzM3B9uF7cYI924eQR00tUGKskae'
    intent = stripe.PaymentIntent.create(

        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )

    return render(request, 'payment/home.html', {'client_secret': intent.client_secret})


@csrf_exempt
# def stripe_webhook(request):
#     payload = request.body
#     event = None
#
#     try:
#         event = stripe.Event.construct_from(
#             json.loads(payload), stripe.api_key
#         )
#     except ValueError as e:
#         print(e)
#         return HttpResponse(status=400)
#
#     # Handle the event
#     if event.type == 'payment_intent.succeeded':
#         payment_confirmation(event.data.object.client_secret)
#
#     else:
#         print('Unhandled event type {}'.format(event.type))
#
#     return HttpResponse(status=200)

def order_placed(request):
    basket = Basket(request)
    basket.clear()
    return render(request, 'payment/orderplaced.html')
