from django.contrib import admin
from .models import Product, Order


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_date', 'created_date',)


# Register your models here.
admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
