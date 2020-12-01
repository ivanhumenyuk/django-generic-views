from django.urls import path
from .department.views import *
from .employee.views import *

urlpatterns = [
    path('', DepartmentList.as_view(), name='department_list_url'),
    path('create/', DepartmentCreate.as_view(), name='department_create_url'),
    path('<int:department_id>/delete/', DepartmentDelete.as_view(), name='department_delete_url'),
    path('<int:department_id>/edit/', DepartmentEdit.as_view(), name='department_edit_url'),
    path('<int:department_id>/employee/list', EmployeeList.as_view(), name='employee_list_url'),
    path('<int:department_id>/employee/add', EmployeeAdd.as_view(), name='employee_add_url'),
    path('<int:department_id>/employee/<int:employee_id>/delete', EmployeeDelete.as_view(), name='employee_delete_url'),
    path('<int:department_id>/employee/<int:employee_id>/edit', EmployeeEdit.as_view(), name='employee_edit_url'),
    path('<int:department_id>/employee/<int:employee_id>/info', EmployeeInfo.as_view(), name='employee_info_url')
]
