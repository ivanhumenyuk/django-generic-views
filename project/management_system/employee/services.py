from .models import Employee
from .forms import EmployeeForm


def get_department_id(self, **kwargs):
    department_id = self.kwargs.get('department_id')
    return department_id


def get_employee_id(self, **kwargs):
    employee_id = self.kwargs.get('employee_id')
    return employee_id
