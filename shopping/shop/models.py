from enum import unique
from django.db import models
from django.db.models.fields.files import ImageField
from django.shortcuts import resolve_url
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, unique= True)
    slug = models.SlugField(max_length=250, unique= True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'category', blank = True)

    class meta:
        ordering = ('name',)
        verbose_name = 'category'
       # verbose_name_plural = 'Categories'

    def get_url(self):
        return reverse('shop:products_by_category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank= True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = ImageField(upload_to = 'product', blank = unique)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now = True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
       # verbose_name_plural = 'products'

    def get_url(self):
        return reverse('shop:ProdCatDetail', args = [self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)