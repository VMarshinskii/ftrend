# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_auto_20150525_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='url',
            field=models.CharField(unique=True, max_length=200, verbose_name=b'Url', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='male',
            field=models.CharField(blank=True, max_length=250, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb', choices=[(b'boys', b'\xd0\x94\xd0\xbb\xd1\x8f \xd0\xbc\xd0\xb0\xd0\xbb\xd1\x8c\xd1\x87\xd0\xb8\xd0\xba\xd0\xbe\xd0\xb2'), (b'girls', b'\xd0\x94\xd0\xbb\xd1\x8f \xd0\xb4\xd0\xb5\xd0\xb2\xd0\xbe\xd1\x87\xd0\xb5\xd0\xba')]),
        ),
    ]
