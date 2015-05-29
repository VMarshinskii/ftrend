# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20150525_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='age',
            name='type',
            field=models.CharField(default=b'boys', max_length=200, verbose_name=b'\xd0\x94\xd0\xbb\xd1\x8f \xd0\xba\xd0\xbe\xd0\xb3\xd0\xbe', choices=[(b'\xd0\x9c\xd0\xb0\xd0\xbb\xd1\x8c\xd1\x87\xd0\xb8\xd0\xba\xd0\xb8', b'\xd0\x9c\xd0\xb0\xd0\xbb\xd1\x8c\xd1\x87\xd0\xb8\xd0\xba\xd0\xb8'), (b'\xd0\x94\xd0\xb5\xd0\xb2\xd0\xbe\xd1\x87\xd0\xba\xd0\xb8', b'\xd0\x94\xd0\xb5\xd0\xb2\xd0\xbe\xd1\x87\xd0\xba\xd0\xb8')]),
        ),
    ]
