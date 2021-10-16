from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150, null=True, unique=True)
    price = models.FloatField()
    ecoinfo = models.TextField()
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
