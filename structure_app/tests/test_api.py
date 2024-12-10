from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from structure_app.models import Department


class DepartmentAPITests(TestCase):
    def setUp(self):
        # создаем тестовые данные для отделов и сотрудников, которые будут использоваться в каждом тесте
        self.client = APIClient()
        self.department = Department.objects.create(name='Отдел кринжа')

    def test_department_list_api_status_code(self):
        response = self.client.get(reverse('apidepartment-list')) # выполняем GET-запрос к API-эндпоинту списка отделов
        self.assertEqual(response.status_code, status.HTTP_200_OK) # проверяем, что API возвращает статус 200

    def test_department_list_api_returns_correct_data(self):
        response = self.client.get(reverse('apidepartment-list'))
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['name'], 'Отдел кринжа') # проверяем JSON-ответ, чтобы убедиться, что он содержит правильные данные.
