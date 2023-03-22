from django.contrib import admin

from .models import TestModel

# Register your models here.

class TestModelAdmin(admin.ModelAdmin):
    """
    내장 admin 페이지에 모델 등록 
    """
    model = TestModel


admin.site.register(TestModel, TestModelAdmin)
