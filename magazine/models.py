# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone




class ActiveDiscountManager(models.Manager):

    def get_queryset(self):
        now = timezone.now()
        return super(ActiveDiscountManager, self).get_queryset().filter(date_begin__lt=now, date_end__gt=now)



class Discount(models.Model):
    name = models.CharField(u'Наименование скидки', max_length=64)
    amount = models.PositiveSmallIntegerField(u'Величина, %',)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    discount_object = GenericForeignKey('content_type', 'object_id')

    date_begin = models.DateTimeField(u'Дата начала')
    date_end = models.DateTimeField(u'Дата окончания')

    objects = models.Manager()
    active_discounts = ActiveDiscountManager()

    def __unicode__(self):
        return '"%s" %s%%' % (self.name, self.amount)



class DiscountMixin(models.Model):

    # discounts = GenericRelation(Discount, object_id_field="object_id")

    @property
    def discounts(self):
        item_type = ContentType.objects.get_for_model(self)
        return Discount.active_discounts.filter(content_type=item_type, object_id=self.pk)

    @property
    def max_discount(self):
        return self.discounts.order_by('-amount').first()

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
    discount_amount = models.PositiveSmallIntegerField(u'Скидка, %', default=0)
    # makemigrations not see field 'discount_price'
    price_with_discount = models.DecimalField(u'Цена со скидкой, руб.', max_digits=10, decimal_places=2)

    @property
    def max_discount(self):
        discounts = []

        cat_discount = self.category.max_discount
        discounts.append(cat_discount)

        item_discount = super(Product, self).max_discount
        discounts.append(item_discount)

        max_discount = None
        for d in discounts:
            if d:
                if not max_discount:
                    max_discount = d
                elif d.amount > max_discount.amount:
                    max_discount = d

        return max_discount

    @property
    def discount_price(self):
        d = self.max_discount

        if d:
            return self.price * (100 - d.amount) / 100
        else:
            return self.price



    class Meta:
        ordering = ('category',)

    def __unicode__(self):
        return self.name
