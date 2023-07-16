from django.contrib import admin

# Register your models here.
from .models import ExpenseModel

class ExpenseAdmin(admin.ModelAdmin):
	list_display = ['title','value','date','cash_out']

admin.site.register(ExpenseModel, ExpenseAdmin)