# reward/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ('username', 'phone_number', 'password1', 'password2')

#
# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ('username', 'phone_number', 'password', 'image')
