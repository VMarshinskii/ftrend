# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20150525_0210'),
        ('sale', '0004_sale_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='product_list',
            field=models.ManyToManyField(to='catalog.Product', verbose_name=b'\xd0\xa2\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80\xd1\x8b'),
        ),
    ]
