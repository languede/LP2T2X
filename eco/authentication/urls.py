from django.contrib import admin
from django.urls import path, include
from .views import reward_home, signup


urlpatterns = [
    path('index/', reward_home, name="reward_home"),
    path('login-signup/', signup, name="login-signup"),
    # path('signin', signin, name="signin"),
]
