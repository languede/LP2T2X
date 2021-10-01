# reward/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import User
from phonenumber_field.modelfields import PhoneNumberField


"""
---------------------
CustomUserCreationForm: 
---------------------
description:
    A custom UserCreationForm used to create user in database under admin permission
    inheritance from django.contrib.auth.forms UserCreationForm super class
    add our custom colmun: 
        phone_number,
        green_point,
        image,
"""


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"


"""
---------------------
RegistrationForm: 
---------------------
description:
    A custom Registration form for register page
    form fields {
        'username' is name
        'phone_number' is phone_number
        'password1' is password
        'password2' is password confirmation
    }
    widgets(add Attributes): add placeholder to "username" and "Phone number"
"""


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'phone_number', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone number'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = \
            forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget = \
            forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirmation'})


"""
---------------------
LoginForm: 
---------------------
description:
    A custom form for login page
    form fields {
        'username' is phone_number
        'password' is password
    }
    widgets(add Attributes): add placeholder to "username" and "password1"
"""


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('phone_number', 'password')
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = \
            forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})

# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ('username', 'phone_number', 'password', 'image')
