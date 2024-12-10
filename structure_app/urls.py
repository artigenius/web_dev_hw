from django.urls import path
from . import views
from .views import (
    DepartmentListView, DepartmentDetailView, DepartmentCreateView,
    DepartmentUpdateView, DepartmentDeleteView,
    EmployeeListView, EmployeeDetailView, EmployeeCreateView,
    EmployeeUpdateView, EmployeeDeleteView,
    ProjectListView, ProjectDetailView, ProjectCreateView,
    ProjectUpdateView, ProjectDeleteView,
    user_create_view 
)

urlpatterns = [
    # Добавляем маршрут для главной страницы
    path('', views.home, name='home'),
    path('user/create/', views.user_create_view, name='user-create'),

    # Маршруты для Department
    path('departments/', DepartmentListView.as_view(), name='department-list'),
    path('departments/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
    path('departments/create/', DepartmentCreateView.as_view(), name='department-create'),
    path('departments/<int:pk>/update/', DepartmentUpdateView.as_view(), name='department-update'),
    path('departments/<int:pk>/delete/', DepartmentDeleteView.as_view(), name='department-delete'),

    # Маршруты для Employee
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('employees/create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('employees/<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('employees/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee-delete'),

    # Маршруты для Project
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('projects/create/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),

    # Маршрут для создания пользователя
    path('user/create/', user_create_view, name='user-create'),  # Путь для создания пользователя

]
