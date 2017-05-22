# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Question,Choice

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
     fields = [ 'question_text','pub_date']
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Question)  # 将Question model注册到admin
admin.site.register(Choice)  # 将Choice model注册到admin