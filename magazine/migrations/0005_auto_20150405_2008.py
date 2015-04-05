# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0004_product_price_with_discount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price_with_discount',
            new_name='discount_price',
        ),
    ]
