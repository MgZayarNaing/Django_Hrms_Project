from django.contrib import admin

# Register your models here.
from hr_payroll.models import PayrollModel
admin.site.register(PayrollModel)