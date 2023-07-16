from django.db import models
from hr_employees.models import EmployeeModel
from hr_tags.models import EmployeeTagModel

# Create your models here.

class PayrollModel(models.Model):
	name = models.CharField(max_length=20, verbose_name='Name')
	salary = models.FloatField(verbose_name='Salary',default=0.0)
	ot_rate = models.IntegerField( verbose_name='Ot Rate',default=0)
	allowance = models.IntegerField( verbose_name='Allowance',default=0)
	deduction = models.IntegerField( verbose_name='Deduction',default=0)
	employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE, default=None)
	tags = models.ManyToManyField(EmployeeTagModel)

	def __str__(self):
		return self.name