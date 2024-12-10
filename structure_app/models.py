from django.db import models
from django.contrib.auth.models import User # импортируем класс пользователя

# Create your models here.
class Department(models.Model):
    name=models.CharField(
        max_length=64,
        unique=True,
        help_text='Название департамента или отдела'
    )
    description=models.TextField(
        help_text='Описание отдела',
        blank=True
    )
    manager=models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='managed_departments',
        help_text='Пользователь, который управляет отделом'
    )
    
    def __str__ (self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='employee_profile',
        help_text='Пользователь системы'
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='employees',
        help_text='Отдел, в котором работает сотрудник'
    )
    position = models.CharField(
        max_length=128,
        help_text='Должность сотрудника',
        blank=True
    )
    hire_date = models.DateField(
        help_text='Дата приема на работу',
        null=True,
        blank=True
    )
    def __str__(self):
        department_name = self.department.name if self.department else 'Без отдела'
        return f"{self.user.username} ({department_name})"

class Project(models.Model):
    name = models.CharField(
        max_length=128,
        unique=True,
        help_text='Название проекта'
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='projects',
        help_text='Отдел, ответственный за проект'
    )
    description = models.TextField(
        help_text='Описание проекта',
        blank=True
    )
    start_date = models.DateField(
        help_text = 'Дата начала проекта'
    )
    end_date = models.DateField(
        help_text='Дата завершения проекта',
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        default=True,
        help_text='Активен ли проект'
    )
