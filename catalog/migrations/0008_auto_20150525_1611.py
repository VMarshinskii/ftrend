# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20150525_0210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
                'verbose_name': '\u0412\u043e\u0437\u0440\u0430\u0441\u0442',
                'verbose_name_plural': '\u0412\u043e\u0437\u0440\u0430\u0441\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
                'verbose_name': '\u0411\u0440\u0435\u043d\u0434',
                'verbose_name_plural': '\u0411\u0440\u0435\u043d\u0434\u044b',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='age',
            field=models.ForeignKey(verbose_name=b'\xd0\x92\xd0\xbe\xd0\xb7\xd1\x80\xd0\xb0\xd1\x81\xd1\x82', blank=True, to='catalog.Age', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(verbose_name=b'\xd0\x91\xd1\x80\xd0\xb5\xd0\xbd\xd0\xb4', blank=True, to='catalog.Brand', null=True),
        ),
    ]
