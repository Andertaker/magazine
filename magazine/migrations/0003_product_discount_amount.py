# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0002_auto_20150404_0425'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_amount',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='\u0421\u043a\u0438\u0434\u043a\u0430, %'),
            preserve_default=True,
        ),
    ]
