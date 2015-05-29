# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20150520_1728'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name': '\u0426\u0432\u0435\u0442', 'verbose_name_plural': '\u0426\u0432\u0435\u0442\u0430'},
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
        ),
    ]
