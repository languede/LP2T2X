from django.contrib import admin
from django.urls import path, include
from .views import home, signup, signin


urlpatterns = [
    path('', home, name="home"),
    path('signup', signup, name="signup"),
    path('signin', signin, name="signin"),
]
