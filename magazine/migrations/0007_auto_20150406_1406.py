# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0006_auto_20150406_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.DecimalField(verbose_name='\u0426\u0435\u043d\u0430 \u0441\u043e \u0441\u043a\u0438\u0434\u043a\u043e\u0439, \u0440\u0443\u0431.', editable=False, max_digits=10, decimal_places=2, db_index=True),
            preserve_default=True,
        ),
    ]
