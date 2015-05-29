# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_age_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='age',
            name='type',
            field=models.IntegerField(default=b'0', verbose_name=b'\xd0\x94\xd0\xbb\xd1\x8f \xd0\xba\xd0\xbe\xd0\xb3\xd0\xbe', choices=[(0, b'\xd0\x9c\xd0\xb0\xd0\xbb\xd1\x8c\xd1\x87\xd0\xb8\xd0\xba\xd0\xb8'), (1, b'\xd0\x94\xd0\xb5\xd0\xb2\xd0\xbe\xd1\x87\xd0\xba\xd0\xb8')]),
        ),
    ]
