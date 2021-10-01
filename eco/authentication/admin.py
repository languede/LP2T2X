from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm
# from .forms import CustomUserChangeForm


"""
---------------------
CustomUserAdmin: 
---------------------
description:
    inheritance from django UserAdmin
    create a Table User to store user accounts in database
    extends system UserAdmin with custom columns/fields:
        'phone_number',
        'green_point',
        'image',
"""


class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Addition features',
            {
                'fields': (
                    'phone_number',
                    'green_point',
                    'image',
                )
            }
        )
    )


admin.site.register(User, CustomUserAdmin)
