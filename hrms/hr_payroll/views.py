from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from hr_payroll import models
from hr_payroll import forms
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator

class PayrollListView(LoginRequiredMixin,ListView):
	login_url = 'login'
	paginate_by = 10
	success_url = reverse_lazy("payroll_list")
	model = models.PayrollModel
	context_object_name = 'all_payrolls'
	template_name = 'payroll_list.html'
    
class PayrollCreateView(PermissionRequiredMixin,CreateView):
	permission_required = 'hr_payroll.add_payrollmodel'
	login_url = 'login'
	success_url = reverse_lazy("payroll_list")
	model = models.PayrollModel
	form_class = forms.PayrollForm
	template_name = 'payroll_create.html'

class PayrollUpdateView(PermissionRequiredMixin,UpdateView):
	permission_required = 'hr_payroll.change_payrollmodel'
	login_url = 'login'
	success_url = reverse_lazy("payroll_list")
	model = models.PayrollModel
	form_class = forms.PayrollForm
	context_object_name = "payroll"
	template_name = 'payroll_update.html'

class PayrollDetailView(PermissionRequiredMixin,DetailView):
	permission_required = 'hr_payroll.view_payrollmodel'
	login_url = 'login'
	model = models.PayrollModel
	context_object_name = "payroll"
	template_name = 'payroll_detail.html'

class PayrollDeleteView(PermissionRequiredMixin,DeleteView):
	permission_required = 'hr_payroll.delete_payrollmodel'
	login_url = 'login'
	# success_url = reverse_lazy("Payroll_list")
	# model = models.PayrollModel
	# context_object_name = "Payroll"
	# template_name = 'Payroll_delete.html'

	def get(self, request, pk):
		Payroll = models.PayrollModel.objects.get(id=pk)
		Payroll.delete()
		return redirect('payroll_list')