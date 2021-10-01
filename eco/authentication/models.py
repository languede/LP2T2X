from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from simple_history.models import HistoricalRecords


# Create your models here.
class User(AbstractUser):
    pass
    # username = models.CharField(max_length=100)
    # password = models.CharField(max_length=50)
    image = models.ImageField(blank=True)
    phone_number = PhoneNumberField(unique=True)
    green_point = models.IntegerField(blank=True, default=0)
    history = HistoricalRecords()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username']
    # test
    def __str__(self):
        return self.username
