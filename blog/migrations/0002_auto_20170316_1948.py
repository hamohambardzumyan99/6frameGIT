# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='free',
            name='image',
            field=models.ImageField(upload_to='image/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='paid',
            name='image',
            field=models.ImageField(upload_to='image/%Y/%m/%d'),
        ),
    ]
