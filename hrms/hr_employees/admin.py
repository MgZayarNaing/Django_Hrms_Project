from django.contrib import admin

# Register your models here.
from hr_employees.models import EmployeeModel
# from app_name.file_name import class_name

admin.site.register(EmployeeModel)