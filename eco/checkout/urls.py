"""eco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages.views import *
from products.views import *
from checkout.views import *
from django.conf.urls.static import static
from django.conf import settings
from reward.views import reward_home_view, login_signup_view, user_profile_view

urlpatterns = [
    path('payment_method/', payment_method_view, name='payment_method'),
    path('shopping_cart/', shopping_cart_view, name='shopping_cart'),
    path('checkout/', start_page_view, name='start_page'),
    path('logout', start_page_view, name='logout'),
]
