# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 13:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizz', '0004_auto_20170824_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='criador',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
