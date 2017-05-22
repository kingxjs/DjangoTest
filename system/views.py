# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

# Create your views here.
from system.models import SystemSupplierType,SystemSupplier


def index(request):
    supplier_type_list = SystemSupplierType.objects.filter().order_by("suppliertype_sort")
    context = {'supplier_type_list': supplier_type_list}
    return render(request, 'system/index.html', context)


def detail(request, supplier_type_id=None):
    if supplier_type_id:
        supplier_type = get_object_or_404(SystemSupplierType, pk=supplier_type_id)
    else:
        supplier_type=False
    return render(request, 'system/detail.html', {'supplier_type': supplier_type})
