from django.contrib import admin

# Register your models here.

from . models import Company, EmployeeAssets, Asset

admin.site.register(Company)
admin.site.register(EmployeeAssets)
admin.site.register(Asset)

