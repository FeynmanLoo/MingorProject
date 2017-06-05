# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('extension', models.CharField(max_length=255)),
                ('size', models.IntegerField()),
                ('type', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='images')),
            ],
        ),
    ]