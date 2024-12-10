from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):  # Только list и detail
    queryset = User.objects.all()
    serializer_class = UserSerializer

from django.db.models import Count
from rest_framework.decorators import action
from rest_framework.response import Response
from structure_app.models import Department
from .serializers import DepartmentSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    @action(detail=False, methods=['get'])
    def many_employees(self, request):
        # Считаем количество сотрудников в каждом отделе
        departments = Department.objects.annotate(employee_count=Count('employees')).order_by('-employee_count', 'id')[:10]
        data = [{'id': dept.id, 'name': dept.name, 'employee_count': dept.employee_count} for dept in departments]
        return Response(data)