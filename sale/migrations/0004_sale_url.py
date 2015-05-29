# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0003_auto_20150517_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='url',
            field=models.CharField(default=b'', max_length=200, verbose_name=b'Url'),
        ),
    ]
