# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4\xd0\xb8\xd0\xbc\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sale',
            name='image',
            field=models.ImageField(upload_to=b'static/uploads/', verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
            preserve_default=True,
        ),
    ]
