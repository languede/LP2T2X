from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.conf import settings


# Create your models here.
class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(eco='yes')


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    feature = models.TextField(blank=True)
    title = models.CharField(max_length=255)
    producer = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    greenpoint = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    ecoinfo = models.TextField(blank=True, null=True)
    eco = models.CharField(max_length=100, default='null')
    objects = models.Manager()
    products = models.Manager()

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('title',)

    def get_absolute_url(self):
        temp = reverse('store:product_detail', args=[self.category, self.slug])
        return reverse('store:product_detail', args=[self.category, self.slug])

    def __str__(self):
        return self.title
