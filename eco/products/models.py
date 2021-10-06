from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(default='this is cool')
    ecological = models.BooleanField(default=False)
    barcode = models.IntegerField(null=True)
