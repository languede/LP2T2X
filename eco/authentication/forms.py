# reward/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import User
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"
        # fields = ('username', 'phone_number', 'password1', 'password2')


class RegistrationForm(UserCreationForm):
    # phone_number = PhoneNumberField(help_text='Required. add a valid phone number')

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


class LoginForm(AuthenticationForm):
    # phone_number = PhoneNumberField(help_text='Required. add a valid phone number')
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
