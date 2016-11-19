# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-19 18:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20161114_2103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.TextField(max_length=50)),
                ('image_alt', models.TextField(max_length=200)),
                ('image_path', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Image_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Image')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Post')),
            ],
        ),
    ]