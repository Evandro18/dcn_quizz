# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pergunta',
            name='alternativa',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
