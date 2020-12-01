from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView
from .forms import EmployeeForm
from .models import Employee
from management_system.department.models import Department
from .services import *


class EmployeeList(ListView):
    model = Employee
    template_name = 'employee/employee_list.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['department_id'] = self.kwargs.get('department_id')
        return data

    def get_queryset(self):
        department = get_object_or_404(Department, pk=self.kwargs['department_id'])
        employee_data = Employee.objects.filter(department=department)
        return employee_data


class EmployeeAdd(CreateView):
    model = Employee
    form_class = EmployeeForm
    pk_url_kwarg = 'department_id'
    template_name = 'employee/employee_add.html'

    def get_initial(self):
        initial = super(EmployeeAdd, self).get_initial()
        initial = initial.copy()
        initial['department'] = get_department_id(self)
        return initial

    def get_context_data(self, **kwargs):
        data = super(EmployeeAdd, self).get_context_data(**kwargs)
        data['department_id'] = get_department_id(self)
        print(data)
        return data

    def get_success_url(self):
        return reverse('employee_list_url',
                       kwargs={'department_id': get_department_id(self)}
                       )


class EmployeeDelete(DeleteView):
    model = Employee
    pk_url_kwarg = 'employee_id'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('employee_list_url',
                       kwargs={'department_id': get_department_id(self)}
                       )


class EmployeeEdit(UpdateView):
    model = Employee
    form_class = EmployeeForm
    pk_url_kwarg = 'employee_id'
    template_name = 'employee/employee_edit.html'

    def get_initial(self):
        initial = super(EmployeeEdit, self).get_initial()
        initial = initial.copy()
        initial['department'] = get_department_id(self)
        return initial

    def get_context_data(self, **kwargs):
        data = super(EmployeeEdit, self).get_context_data(**kwargs)
        data['department_id'] = get_department_id(self)
        data['employee_id'] = get_employee_id(self)
        return data

    def get_success_url(self):
        return reverse('employee_list_url',
                       kwargs={'department_id': get_department_id(self)})


class EmployeeInfo(DetailView):
    template_name = 'employee/employee_info.html'
    model = Employee
    pk_url_kwarg = 'employee_id'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['department_id'] = get_department_id(self)
        return data



