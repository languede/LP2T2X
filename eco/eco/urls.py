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
from reward.views import login_signup_view

urlpatterns = [
    path('', home_view, name='home'),
    path('', include('reward.urls')),
    path('home/', home_view, name='home'),
    path('login/', login_signup_view, name='login-signup'),
    path('create/', product_create_view, name='create'),
    path('about_us/', about_us_view, name='about_us'),
    path('details/', product_detail_view, name='details'),
    path('checkout/', checkout_view, name='checkout'),
    path('product/', product_detail_view, name='product'),
    # checkout page
    path('payment_method/', payment_method_view, name='payment_method'),
    path('shopping_cart/', shopping_cart_view, name='shopping_cart'),
    path('start_page/', start_page_view, name='start_page'),
    # admin
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
