from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from hr_expense import models
from hr_expense import forms
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator

class ExpenseListView(LoginRequiredMixin,ListView):
	login_url = 'login'
	paginate_by = 10
	model = models.ExpenseModel
	template_name = 'expense_list.html'
	context_object_name = "expense_list"

class ExpenseCreateView(PermissionRequiredMixin,CreateView):
	permission_required = 'hr_expense.add_expensemodel'
	login_url = 'login'
	success_url = reverse_lazy("expense_list")
	model = models.ExpenseModel
	form_class = forms.ExpenseForm
	template_name = 'expense_create.html'

class ExpenseUpdateView(PermissionRequiredMixin,UpdateView):
	permission_required = 'hr_expense.change_expensemodel'
	login_url = 'login'
	success_url = reverse_lazy("expense_list")
	model = models.ExpenseModel
	form_class = forms.ExpenseForm
	context_object_name = "expense"
	template_name = 'expense_update.html'

class ExpenseDeleteView(PermissionRequiredMixin,DeleteView):
	permission_required = 'hr_expense.view_expensemodel'
	login_url = 'login'
	# model = models.ExpenseModel
	# context_object_name = "expense"
	# template_name = 'expense_delete.html'

	def get(self, request, pk):
		resume = models.ExpenseModel.objects.get(id=pk)
		resume.delete()
		return redirect('expense_list')

class ExpenseDetailView(DetailView):
	permission_required = 'hr_expense.view_expensemodel'
	login_url = 'login'
	model = models.ExpenseModel
	context_object_name = "expense"
	template_name = 'expense_detail.html'

	