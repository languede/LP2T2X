from django.db import models
from simple_history.models import HistoricalRecords
from datetime import datetime


class Product(models.Model):
    # Product Table: store all product data
    name = models.CharField(max_length=120)
    image = models.ImageField(blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=4294967295)
    summary = models.TextField(default='this is cool')
    is_eco = models.BooleanField(default=False)
    barcode = models.IntegerField(null=True)


class Order(models.Model):
    # Order recoder Table: store all order information from customer each time
    user_id = models.CharField(max_length=120)
    order_items = models.JSONField()
    total_point = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=4294967295)
    order_date = models.DateTimeField(auto_now_add=True)
