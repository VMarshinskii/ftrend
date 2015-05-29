# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20150525_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='age',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name=b'\xd0\x92\xd0\xbe\xd0\xb7\xd1\x80\xd0\xb0\xd1\x81\xd1\x82', choices=[(1, '\u043e\u0442 2-x \u043b\u0435\u0442')]),
        ),
    ]
