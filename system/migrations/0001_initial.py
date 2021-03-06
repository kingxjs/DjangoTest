# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 03:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SystemSupplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SystemSupplierType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suppliertype_name', models.CharField(max_length=200)),
                ('suppliertype_sort', models.IntegerField(default=0)),
                ('suppliertype_status', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='systemsupplier',
            name='supplier_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.SystemSupplierType'),
        ),
    ]
