from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Todo


# Create your tests here.
class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title='Complete the alx course',
            body='Hard things don tire me abeg'
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, 'Complete the alx course')
        self.assertEqual(self.todo.body, 'Hard things don tire me abeg')
        self.assertEqual(str(self.todo), 'Complete the alx course')

    def test_api_listview(self):
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, 'Complete the alx course')
