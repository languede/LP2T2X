from django.contrib import admin
from django.urls import path, include
from .views import reward_home_view, login_signup_view, add_green_points_view, user_profile_view


urlpatterns = [
    path('index/', reward_home_view, name="reward_home"),
    path('login-signup/', login_signup_view, name="login-signup"),
    path('profile/<id>', add_green_points_view, name="green_points"),
    path('profile/', user_profile_view, name="profile"),
    # path('signin', signin, name="signin"),
]
