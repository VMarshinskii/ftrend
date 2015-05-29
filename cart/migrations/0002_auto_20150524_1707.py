# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.AddField(
            model_name='cartproduct',
            name='cart',
            field=models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xbe\xd1\x80\xd0\xb7\xd0\xb8\xd0\xbd\xd0\xb0', to='cart.Cart', null=True),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='color',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\xa6\xd0\xb2\xd0\xb5\xd1\x82', blank=True),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='count',
            field=models.IntegerField(verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe', blank=True),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='size',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb7\xd0\xbc\xd0\xb5\xd1\x80', blank=True),
        ),
    ]
