# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curves', '0002_auto_20150414_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_specific',
            name='prof',
            field=models.CharField(max_length=200),
        ),
    ]
