from django.contrib import admin
from django.urls import path, include
from .views import reward_home, login_signup, signup


urlpatterns = [
    path('index/', reward_home, name="reward_home"),
    path('login-signup/', login_signup, name="login-signup"),
    # path('signin', signin, name="signin"),
]
