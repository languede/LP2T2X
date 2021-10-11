from django.shortcuts import render
from .forms import *


# Create your views here.
def product_detail_view(request):
    barcode_html = request.GET.get("barcode")
    products = Product.objects.get(barcode=barcode_html)
    context = {
        'product': products
    }
    return render(request, "product/product_detail.html", context)


def product_create_view(request):
    my_form = RawProductForm()
    if request.method == "POST":
        my_form = RawProductForm(request.POST, request.FILES)
        if my_form.is_valid():
            # now the data is good
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        'form': my_form
    }
    return render(request, "product/product_create.html", context)


# def product_create_view(request):
#     my_form = ProductForm(request.POST or None)
#     if my_form.is_valid():
#         my_form.save()
#         context = {
#             'form': my_form
#         }
#     return render(request, "product/product_create.html", context)
