from django.urls import path
from . import views

urlpatterns = [
    # Leave as empty string for base url
    path('eco_product_details/', views.store, name="product_details"),
    path('cart/<product_id>', views.cart, name="cart"),
]
