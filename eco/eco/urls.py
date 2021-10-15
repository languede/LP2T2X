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
# from reward.views import reward_home_view, login_signup_view, user_profile_view

urlpatterns = [
    # base templates
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
    # path('login/', login_signup_view, name='login-signup'),
    path('create/', product_create_view, name='create'),
    path('about_us/', about_us_view, name='about_us'),
    # product app
    path('', include('products.urls')),
    # checkout app
    path('', include('checkout.urls')),
    # reward system app
    path('', include('reward.urls')),
    # store app
    path('', include('store.urls')),
    # basket app
    path('', include('basket.urls')),
    # admin
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
