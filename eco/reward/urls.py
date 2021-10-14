from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('index/', views.reward_home_view, name="reward_home"),
    path('login/', views.loginUser, name="login"),
    path('register/', views.registerUser, name="register"),


    # path('login-signup/', views.login_signup_view, name="login-signup"),
    path('logout/', views.logoutUser, name="logout"),
    path('profile/', views.user_profile_view, name="profile"),

    path('rating/', views.eco_rating_view, name="rating"),
]
