# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-26 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailuser_id', models.IntegerField()),
                ('activation_key', models.CharField(max_length=40, verbose_name='activation key')),
            ],
            options={
                'verbose_name': 'registration profile',
                'verbose_name_plural': 'registration profiles',
            },
        ),
    ]
