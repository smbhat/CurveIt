# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curves', '0005_auto_20150415_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_specific',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='course_specific',
            name='prof',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
