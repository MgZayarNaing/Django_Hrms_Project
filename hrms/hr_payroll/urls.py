from django.urls import path
from hr_payroll import views

urlpatterns = [
	path('show_payroll/', views.PayrollListView.as_view(), name='payroll_list'),
	path('new_payroll/', views.PayrollCreateView.as_view(), name='payroll_create'),
	path('update/<int:pk>/', views.PayrollUpdateView.as_view(), name='payroll_update'),
	path('detail/<int:pk>/', views.PayrollDetailView.as_view(), name='payroll_detail'),
	path('delete/<int:pk>/', views.PayrollDeleteView.as_view(), name='payroll_delete'),
	# path('search_by/', views.SearchBy.as_view()),
    # path('order_by/', views.OrderBy.as_view())
]