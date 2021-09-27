from django.contrib import admin
from django.urls import path, include
from .views import home


urlpatterns = [
    path('', home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
]
