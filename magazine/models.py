# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType



class Discount(models.Model):
    name = models.CharField(u'Наименование скидки', max_length=64)
    amount = models.PositiveSmallIntegerField(u'Величина, %',)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    discount_object = GenericForeignKey('content_type', 'object_id')

    date_begin = models.DateTimeField(u'Дата начала')
    date_end = models.DateTimeField(u'Дата окончания')

    def __unicode__(self):
        return '"%s" %s%%' % (self.name, self.amount)



class DiscountMixin(models.Model):

    discounts = GenericRelation(Discount, object_id_field="object_id")

#    def get_discounts(self):
#        return

    class Meta:
        abstract = True



class Category(DiscountMixin):
    name = models.CharField(u'Категория товара', max_length=64)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name



class Product(DiscountMixin):
    category = models.ForeignKey(Category, verbose_name=u'Категория', related_name="products")
    name = models.CharField(u'Наименование товара', max_length=128)
    price = models.DecimalField(u'Цена единицы, руб.', max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('category',)

    def __unicode__(self):
        return self.name
