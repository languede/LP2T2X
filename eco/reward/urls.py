from django.contrib import admin
from django.urls import path, include
from .views import reward_home_view, login_signup_view, signup


urlpatterns = [
    path('index/', reward_home_view, name="reward_home"),
    path('login-signup/', login_signup_view, name="login-signup"),
    # path('signin', signin, name="signin"),
]
