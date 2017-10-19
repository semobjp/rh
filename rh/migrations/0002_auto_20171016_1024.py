# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 13:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rh', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='senha',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='usuario',
        ),
        migrations.AddField(
            model_name='funcionario',
            name='user',
            field=models.OneToOneField(default=-1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]