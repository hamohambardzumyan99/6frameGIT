# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170316_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='free',
            name='YouTube_link',
            field=models.CharField(max_length=250, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paid',
            name='YouTube_link',
            field=models.CharField(max_length=250, default=''),
            preserve_default=False,
        ),
    ]
