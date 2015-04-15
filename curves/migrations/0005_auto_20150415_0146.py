# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curves', '0004_auto_20150415_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='year',
            field=models.CharField(default=b'', max_length=4),
        ),
        migrations.AlterField(
            model_name='user',
            name='netid',
            field=models.CharField(max_length=50),
        ),
    ]
