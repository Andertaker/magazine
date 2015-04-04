# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('magazine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0441\u043a\u0438\u0434\u043a\u0438')),
                ('amount', models.PositiveSmallIntegerField(verbose_name='\u0412\u0435\u043b\u0438\u0447\u0438\u043d\u0430, %')),
                ('object_id', models.PositiveIntegerField()),
                ('date_begin', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430')),
                ('date_end', models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('category',)},
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(related_name=b'products', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', to='magazine.Category'),
        ),
    ]
