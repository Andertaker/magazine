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


def task_b(request):
    '''
    б) То же самое, но оставить лишь категории, в которых строго больше 10 товаров
    '''

    cats = Category.objects.annotate(num_products=Count('products')).filter(products__price__gt=100, num_products__gt=10)
    for c in cats:
        print c.name, c.num_products


    return HttpResponse('')


def task_c(request):
    '''
    в) Написать код python, который выводит в консоль перечень всех товаров. Каждая строка должна содержать следующие данные:
        название категории товара,
        наименование товара,
        цена.
    По возможности, минимизировать количество обращений к базе данных и количество передаваемых данных
    '''

    products = Product.objects.select_related('category').values('category__name', 'name', 'price')
    for p in products:
        print p


    return HttpResponse('')



def discounts(request):
    c = Category.objects.get(id=4)
    # print c.discounts.all()
    print c.max_discount

    p = Product.objects.get(id=5)
    print p.max_discount



    return HttpResponse('')
