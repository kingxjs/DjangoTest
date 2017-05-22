# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible  # only if you need to support Python 2
class SystemSupplierType(models.Model):
    suppliertype_name = models.CharField(max_length=200)
    suppliertype_sort = models.IntegerField(default=0)
    suppliertype_status=models.IntegerField(default=1)

    def __str__(self):
        return self.suppliertype_name

@python_2_unicode_compatible  # only if you need to support Python 2
class SystemSupplier(models.Model):
    supplier_name = models.CharField(max_length=200)
    supplier_type=models.ForeignKey(SystemSupplierType, on_delete=models.CASCADE)

    def __str__(self):
        return self.supplier_name