from django.shortcuts import render
from .models import Product
from .forms import *


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
