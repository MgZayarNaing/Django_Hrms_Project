from django.db import models

# Create your models here.
from django.utils import timezone
from hr_employees.models import EmployeeModel
from hr_tags.models import EmployeeTagModel

class ExpenseModel(models.Model):
    title = models.CharField(max_length=20, verbose_name='Name')
    value = models.CharField(max_length=16,default='00,000.00')
    date = models.DateField(default=timezone.now)
    cash_out = models.BooleanField(default=False)
    employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE, default=None)
    tags = models.ManyToManyField(EmployeeTagModel)