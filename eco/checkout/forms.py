from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from authentication.models import User
from phonenumber_field.modelfields import PhoneNumberField


class StartForm(AuthenticationForm):
    # phone_number = PhoneNumberField(help_text='Required. add a valid phone number')
    class Meta:
        model = User
        fields = 'phone_number'
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'phone', 'placeholder': 'Please enter your Phone number'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password')
        # self.fields['password'].widget = \
        #     forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
