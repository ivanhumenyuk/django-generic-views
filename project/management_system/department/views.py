from django.shortcuts import reverse, get_object_or_404
from .forms import DepartmentForm
from .models import Department
from django.views.generic import ListView, CreateView, DeleteView, UpdateView


class DepartmentList(ListView):
    model = Department
    template_name = 'department/department_list.html'


class DepartmentCreate(CreateView):
    form_class = DepartmentForm
    template_name = 'department/department_create.html'

    def get_success_url(self):
        return reverse('department_list_url')


class DepartmentDelete(DeleteView):
    model = Department
    pk_url_kwarg = 'department_id'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('department_list_url')


class DepartmentEdit(UpdateView):
    model = Department
    form_class = DepartmentForm
    pk_url_kwarg = 'department_id'
    template_name = 'department/department_edit.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['department_id'] = self.kwargs.get('department_id')
        return data

    def get_success_url(self):
        return reverse('department_list_url')



