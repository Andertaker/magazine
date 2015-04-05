# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0005_auto_20150405_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='date_end',
            field=models.DateTimeField(default=None, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_amount',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='\u0421\u043a\u0438\u0434\u043a\u0430, %', editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.DecimalField(verbose_name='\u0426\u0435\u043d\u0430 \u0441\u043e \u0441\u043a\u0438\u0434\u043a\u043e\u0439, \u0440\u0443\u0431.', editable=False, max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
    ]
