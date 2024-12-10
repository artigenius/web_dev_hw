from django.test import TestCase
from django.urls import reverse


class DepartmentViewTests(TestCase):
    def test_department_list_view_status_code(self):
        response = self.client.get(reverse('department-list')) # симулирует GET-запрос к URL страницы списка отделов
        self.assertEqual(response.status_code, 200) # проверяет, что страница успешно загрузилась (код 200)

    def test_department_list_view_template_used(self):
        response = self.client.get(reverse('department-list'))
        self.assertTemplateUsed(response, 'department/department_list.html') # проверяет, что используется правильный HTML-шаблон

    def test_department_list_view_contains_correct_content(self):
        response = self.client.get(reverse('department-list'))
        self.assertContains(response, 'Список отделов') #  проверяет, что в HTML-ответе присутствует определенный текст (например, "Список отделов")


