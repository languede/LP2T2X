from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm
# from .forms import CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Phone Number',
            {
                'fields': (
                    'phone_number',
                    'image',
                )
            }
        )
    )


admin.site.register(User, CustomUserAdmin)
