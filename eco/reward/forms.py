# reward/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from authentication.models import User

class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'phone_number', 'email']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)


class ResetPasswordForm(ModelForm):
    class Meta:
        model = User
        fields = ['password']

    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = \
            forms.PasswordInput(attrs={'placeholder': 'Password'})