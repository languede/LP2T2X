from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass
    # username = models.CharField(max_length=100)
    # password = models.CharField(max_length=50)
    image = models.ImageField(blank=True)
    phone_number = PhoneNumberField(unique=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

