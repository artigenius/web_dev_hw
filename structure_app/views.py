from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Department, Employee, Project
from django.urls import reverse_lazy

# Представления для Department
class DepartmentListView(ListView):
    model = Department
    template_name = 'department/department_list.html'
    context_object_name = 'departments'

class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'department/department_detail.html' 
    context_object_name = 'department'

    def get_context_data(self, **kwargs):
        # Получаем контекст из родительского класса
        context = super().get_context_data(**kwargs)

        # Получаем проекты, связанные с этим отделом
        department = self.get_object()
        active_projects = Project.objects.filter(department=department, is_active=True)  # Активные проекты
        closed_projects = Project.objects.filter(department=department, is_active=False)  # Закрытые проекты

        # Добавляем проекты в контекст
        context['active_projects'] = active_projects
        context['closed_projects'] = closed_projects
        return context

class DepartmentCreateView(CreateView):
    model = Department
    fields = ['name', 'description', 'manager']
    template_name = 'department/department_form.html' 
    success_url = '/departments/'

class DepartmentUpdateView(UpdateView):
    model = Department
    fields = ['name', 'description', 'manager']
    template_name = 'department/department_form.html' 
    success_url = '/departments/'

class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'department/department_confirm_delete.html'  
    success_url = reverse_lazy('department-list')

# Представления для Employee
class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee/employee_list.html' 
    context_object_name = 'employees'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee/employee_detail.html'  
    context_object_name = 'employee'

class EmployeeCreateView(CreateView):
    model = Employee
    fields = ['user', 'department', 'position', 'hire_date']
    template_name = 'employee/employee_form.html'  
    success_url = '/employees/'

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['user', 'department', 'position', 'hire_date']
    template_name = 'employee/employee_form.html'  
    success_url = '/employees/'

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee/employee_confirm_delete.html'  
    success_url = '/employees/'

# Представления для Project
class ProjectListView(ListView):
    model = Project
    template_name = 'project/projects_list.html'  
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project/project_detail.html'  
    context_object_name = 'project'

class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'department', 'description', 'start_date', 'end_date', 'is_active']
    template_name = 'project/project_form.html'  
    success_url = '/projects/'

class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['name', 'department', 'description', 'start_date', 'end_date', 'is_active']
    template_name = 'project/project_form.html'  
    success_url = '/projects/'

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project/project_confirm_delete.html'  
    success_url = '/projects/'

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Представление для создания нового пользователя
def user_create_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправляем на главную страницу после успешного создания пользователя
    else:
        form = UserCreationForm()

    return render(request, 'user/user_create.html', {'form': form})

from django.shortcuts import render

# Главная страница
def home(request):
    return render(request, 'home.html')

