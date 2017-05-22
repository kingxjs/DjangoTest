# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from system.models import SystemSupplierType, SystemSupplier

admin.site.register(SystemSupplierType)  # 将Choice model注册到admin
admin.site.register(SystemSupplier)  # 将Choice model注册到admin