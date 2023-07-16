
from django import forms
from django.forms import widgets
from .models import ExpenseModel


class ExpenseForm(forms.ModelForm):
	class Meta:
		model = ExpenseModel
		fields = "__all__"
		labels = {
			'title':'Enter Title',
			'value':'Value',
			'date':'Enter Date',
			'expense': 'Employee',
            'tags': 'Tags'
		}
		widgets = {
			'title': widgets.TextInput(attrs={'placeholder':'Name', 'class': 'form-control'}),
			'value': widgets.NumberInput(attrs={'placeholder':'0', 'class': 'form-control'}),
			'date': widgets.DateInput(attrs={'placeholder':' Date', 'type': 'date', 'class': 'form-control'}),
			'employee': widgets.Select(attrs={'class': 'form-control'}),
            'tags': widgets.CheckboxSelectMultiple()
		}