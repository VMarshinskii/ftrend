# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_auto_20150525_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043b\u043b\u0435\u043a\u0446\u0438\u044f',
                'verbose_name_plural': '\u041a\u043e\u043b\u043b\u0435\u043a\u0446\u0438\u0438',
            },
        ),
        migrations.AlterModelOptions(
            name='age',
            options={'verbose_name': '\u0412\u043e\u0437\u0440\u0430\u0441\u0442', 'verbose_name_plural': '\u0412\u043e\u0437\u0440\u0430\u0441\u0442'},
        ),
        migrations.AddField(
            model_name='product',
            name='code',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xb4 \xd1\x82\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x80\xd0\xb0', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='country',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\xa1\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb0 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb8\xd0\xb7\xd0\xb2\xd0\xbe\xd0\xb4\xd1\x81\xd1\x82\xd0\xb2\xd0\xb0', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='growth',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\xa0\xd0\xbe\xd1\x81\xd1\x82', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='included',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\x92 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbf\xd0\xbb\xd0\xb5\xd0\xba\xd1\x82\xd0\xb5', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='male',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='size_label',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb7\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xbd\xd0\xb0 \xd1\x8d\xd1\x82\xd0\xb8\xd0\xba\xd0\xb5\xd1\x82\xd0\xba\xd0\xb5', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='structure',
            field=models.CharField(max_length=250, verbose_name=b'\xd0\xa1\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'\xd0\x91\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb4', blank=True, to='catalog.Brand', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_sale',
            field=models.IntegerField(default=0, verbose_name=b'\xd0\xa6\xd0\xb5\xd0\xbd\xd0\xb0 \xd1\x81\xd0\xbe \xd1\x81\xd0\xba\xd0\xb8\xd0\xb4\xd0\xba\xd0\xbe\xd0\xb9', editable=False),
        ),
        migrations.AddField(
            model_name='product',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbb\xd0\xbb\xd0\xb5\xd0\xba\xd1\x86\xd0\xb8\xd1\x8f', blank=True, to='catalog.Collection', null=True),
        ),
    ]
