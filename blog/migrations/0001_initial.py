# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Free',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(verbose_name='date published')),
                ('image', models.ImageField(upload_to='video/%Y/%m/%d')),
                ('download_url', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Paid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(verbose_name='date published')),
                ('image', models.ImageField(upload_to='video/%Y/%m/%d')),
                ('price', models.CharField(max_length=250)),
            ],
        ),
    ]
