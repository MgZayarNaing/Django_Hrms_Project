from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import EmployeeModel
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from hr_jobs.models import JobModel
from django.core.paginator import Paginator
from hr_tags.models import EmployeeTagModel

def search_by(request):
    search = request.GET.get('search')
    if search:    
        employees = EmployeeModel.objects.filter(
            Q(name__icontains=search) | 
            Q(age__icontains=search) |
            Q(birthday__icontains=search) |
            Q(address__icontains=search) |
            Q(email__icontains=search) |
            Q(gender__icontains=search) |
            Q(joining_date__icontains=search)
        )
    else:      
        employees = EmployeeModel.objects.all()
    return render(request, 'employee_list.html', {'page_obj': employees})

def order_by(request):
    print('order by call')
    order = request.GET.get('order')
    employees = EmployeeModel.objects.all().order_by("-" + order)
    order_selected = {str(order): 'btn-primary text-white'}
    paginator = Paginator(employees, 10) # Show 2 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'employee_list.html', {'page_obj': page_obj, 'order_selected': order_selected})

@permission_required('hr_employees.view_employeemodel', login_url='login')
def employee(request, employee_id):
	print('employee call ++++++++++++++++++++')
	print('employee_id ', employee_id)
	if request.method == "GET":
		print('employee GET call')
		employee = EmployeeModel.objects.get(id=employee_id)
		return render(request,'employee_detail.html', {'employee': employee})

@login_required(login_url='login')
def all_employees(request):
	print('all_employees call ++++++++++++++++++++')
	if request.method == "GET":
		print('all_employees GET call')
		all_employees = EmployeeModel.objects.all()
		paginator = Paginator(all_employees, 10) # Show 2 contacts per page.
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		return render(request,'employee_list.html', {'page_obj': page_obj})
		#return render(request,'employee_list.html', {'all_employees': all_employees})

@permission_required('hr_employees.add_employeemodel', login_url='login') 
def add_employee(request):
	print('add_employee call ++++++++++++++++++++++')
	if request.method == "GET":
		print('add_employee GET call')
		employee = EmployeeModel()
		jobs = JobModel.objects.all()
		jobs = JobModel.objects.all()
		tags = EmployeeTagModel.objects.all()
		context = {'employee': employee, 'jobs': jobs, 'tags': tags}
		return render(request,'employee_create.html', context )
	if request.method == "POST" and request.FILES['image']:
		print('add_employee POST call')
		print('data => ', request.POST)
		name = request.POST.get('name')
		age = request.POST.get('age')
		birthday = request.POST.get('birthday')
		address = request.POST.get('address')
		email = request.POST.get('email')
		gender = request.POST.get('gender')
		job = request.POST.get('job')
		tags = request.POST.getlist('tags')
		if request.POST.get('is_married') == 'on':
			is_married = True
		else:
			is_married = False
		joining_date = request.POST.get('joining_date')
		image = request.FILES.get('image')
		employee = EmployeeModel.objects.create(
			name=name,
			age=age,
			birthday=birthday,
			address=address,
			email=email,
			gender=gender,
			job_id=job,
			is_married=is_married,
			joining_date=joining_date,
			image=image
		)
		employee.tags.set(tags)
		employee.save()
		return redirect('/hr_employees/show_employee/')

@permission_required('hr_employees.change_employeemodel', login_url='login')
def update_employee(request, employee_id):
	print('update_employee call +++++++++++++++++++++')
	print('employee_id ', employee_id)
	employee = EmployeeModel.objects.get(id=employee_id)
	if request.method == "GET":
		print('update_employee GET call')
		employee.birthday = str(employee.birthday)
		employee.joining_date = datetime.strftime(employee.joining_date, '%Y-%m-%dT%H:%M')
		jobs = JobModel.objects.all()
		tags = EmployeeTagModel.objects.all()
		context = {'employee': employee,'jobs': jobs, 'tags': tags}
		return render(request, 'employee_update.html', context)
	elif request.method == "POST":
		print('update_employee POST call')
		print('data => ', request.POST)
		employee.name = request.POST.get('name')
		employee.age = request.POST.get('age')
		employee.birthday = request.POST.get('birthday')
		employee.address = request.POST.get('address')
		employee.email = request.POST.get('email')
		employee.gender = request.POST.get('gender')
		# employee.is_married = request.POST.get('is_married')
		if request.POST.get('is_married') == 'on':
			employee.is_married = True 
		else:
			employee.is_married = False
		employee.joining_date = request.POST.get('joining_date')
		if request.FILES.get('image'):
			employee.image = request.FILES.get('image')
			employee.job_id = request.POST.get('job')
			employee.tags.set(request.POST.getlist('tags'))
		employee.save()
		return redirect('/hr_employees/detail/' + str(employee_id) + '/')

# def custom_access_right(user):
#     #return user.groups.filter(name='CustomGroup').exists()
#     if user.has_perm('hr_employees.custom_access_right') and user.has_perm('hr_employees.my_access_right'):
#         return True
#     return False

# @user_passes_test(custom_access_right, login_url='login') 
@permission_required('hr_employees.delete_employeemodel', login_url='login')
def delete_employee(request, employee_id):
	print('delete employee call +++++++++++++++')
	print('employee_id ', employee_id)
	if request.method == "GET":
		print('delete_employee GET call')
		employee = EmployeeModel.objects.get(id=employee_id)
	# 	return render(request, 'employee_delete.html', {'employee': employee})
	# if request.method == "POST":
	# 	print('delete_employee POST call')
		employee = EmployeeModel.objects.filter(id=employee_id)
		employee.delete()
		return redirect('/hr_employees/show_employee/')