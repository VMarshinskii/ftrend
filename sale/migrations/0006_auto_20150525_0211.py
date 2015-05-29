# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0005_sale_product_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='product_list',
            new_name='products',
        ),
    ]
