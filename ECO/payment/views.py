import json

import stripe
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from basket.basket import Basket
from django.contrib.auth import get_user_model

User = get_user_model()


# class Error(TemplateView):
#     template_name = 'payment/error.html'


# before payment user be required login
@login_required(login_url='login')
def payByGreenView(request):
    basket_summary = Basket(request)
    total_point_cost = int(basket_summary.get_total_greenpoint())
    user = User.objects.get(id=request.user.id)
    check_user_points_changes = user.green_point - total_point_cost
    context = {"green_points": user.green_point}

    if not basket_summary.basket:
        context["basket"] = bool(basket_summary.basket)
    if check_user_points_changes < 0:
        # no enough points to purchase
        context["no_points"] = True
    if check_user_points_changes >= 0 and basket_summary.basket:
        user.green_point -= total_point_cost
        user.save()
        context["no_points"] = False
        context["basket"] = basket_summary
        basket_summary.clear()

        return render(request, 'payment/orderplaced.html', context)

    return render(request, 'basket/summary.html', context)


# before payment user be required login
@login_required(login_url='login')
def BasketView(request):
    basket_summary = Basket(request)
    total = str(basket_summary.get_total_greenpoint())
    total = total.replace('.', '')
    total = int(total)

    if not basket_summary.basket:
        return render(request, 'basket/summary.html', {"basket": bool(basket_summary.basket)})
    else:
        stripe.api_key = 'sk_test_51JjiBRDJaj9YScNg80KFVH0YXrbzvnoSR4jB0KgmoIyAd34Aa5dZ7i1BKko1IUE7vtAYYzYzM3B9uF7cYI924eQR00tUGKskae'
        intent = stripe.PaymentIntent.create(
            amount=total,
            currency='gbp',
            metadata={'userid': request.user.id})

    return render(request, 'payment/home.html', {'client_secret': intent.client_secret})


def order_placed(request):
    basket = Basket(request)
    content = {'basket': basket}
    basket.clear()
    return render(request, 'payment/orderplaced.html', content)
