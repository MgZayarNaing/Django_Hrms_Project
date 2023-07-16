from django import forms
from django.forms import widgets
from .models import PayrollModel


class PayrollForm(forms.ModelForm):
	class Meta:
		model = PayrollModel
		fields = "__all__"
		labels = {
			'name':'Enter Name',
			'salary':'Enter Salary',
			'ot_rate':'Ot_rate',
			'allowance':' Allowance',
			'deduction':'deduction',
			'payroll': 'Employee',
            'tags': 'Tags'
		}
		widgets = {
			'name': widgets.TextInput(attrs={'placeholder':'Payroll Name', 'class': 'form-control'}),
			'salary': widgets.NumberInput(attrs={'placeholder':'0', 'class': 'form-control'}),
			'ot_rate': widgets.NumberInput(attrs={'placeholder':'0', 'class': 'form-control'}),
			'allowance': widgets.NumberInput(attrs={'placeholder':' 0', 'class': 'form-control'}),
			'deduction': widgets.NumberInput(attrs={'placeholder':' 0', 'class': 'form-control'}),
			'employee': widgets.Select(attrs={'class': 'form-control'}),
            'tags': widgets.CheckboxSelectMultiple()
		}