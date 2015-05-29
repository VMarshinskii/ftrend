# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20150520_1834'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sale',
            new_name='sale_value',
        ),
    ]
