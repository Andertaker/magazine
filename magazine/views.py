# -*- coding: utf-8 -*-
from django.db.models import Count
from django.shortcuts import render_to_response
from django.http.response import HttpResponse

from . models import Category, Product



def task_a(request):
    '''
    а) С помощью Django ORM выбрать товары, цена которых больше или равна 100 руб.,
    сгруппировать по категориям и посчитать количество товаров в каждой категории.
    '''

    cats = Category.objects.annotate(num_products=Count('products')).filter(products__price__gt=100)
    for c in cats:
        print c.name, c.num_products


    return HttpResponse('')
