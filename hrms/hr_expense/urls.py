from django.urls import path
from hr_expense import views

urlpatterns = [

	path('show_expense/', views.ExpenseListView.as_view(), name='expense_list'),
	path('new_expense/', views.ExpenseCreateView.as_view(), name='expense_create'),
	path('update/<int:pk>/', views.ExpenseUpdateView.as_view(), name='expense_update'),
	path('delete/<int:pk>/', views.ExpenseDeleteView.as_view(), name='expense_delete'),
	path('detail/<int:pk>/', views.ExpenseDetailView.as_view(), name='expense_detail'),
]
