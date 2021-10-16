from django.shortcuts import render
from .models import *


# Create your views here.

def cart(request, product_id):
    products = Product.objects.get(pk=product_id)
    # context = {'products':products}
    return render(request, 'Cart.html', {'product': products})


def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'Store.html', context)
