# -*- coding: utf-8 -*-
from django.db import models



class Category(models.Model):
    name = models.CharField(u'Категория товара', max_length=64)



class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name=u'Категория')
    name = models.CharField(u'Наименование товара', max_length=128)
    price = models.DecimalField(u'Цена единицы, руб.', max_digits=10, decimal_places=2)
