from django.contrib.auth.models import User
from rest_framework import serializers
from structure_app.models import Employee 

class UserSerializer(serializers.ModelSerializer):
    organization = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'organization']

    def get_organization(self, obj):
        try:
            # Получаем организацию (отдел) через Employee
            return obj.employee_profile.department.name
        except AttributeError:
            return None

from structure_app.models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'description', 'manager']