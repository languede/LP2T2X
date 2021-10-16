from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Category, Product


# Create your views here.
def categories(request):
    return {
        'categories': Category.objects.all()
        # access category data by using categories
    }


def all_products(request):
    products = Product.objects.all()
    # sql select all product
    return render(request, 'home.html', {'products': products})
    # render loading the template


def product_detail(request, slug, category_slug):
    temp = category_slug
    temp2 = slug
    category = get_object_or_404(Category, name=category_slug)
    product = get_object_or_404(Product, slug=slug)

    return render(request, 'products/detail.html', {'category': category, 'product': product})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'products/category.html', {'category': category, 'products': products})
