from django.test import TestCase
from .models import Task
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status

class TaskModelTest(TestCase):

    def test_string_representation(self):
        task = Task(title="Test Task")
        self.assertEqual(str(task), "Test Task")

    def test_create_task(self):
        task = Task.objects.create(title="Unit Test Task", description="Test description")
        self.assertEqual(task.title, "Unit Test Task")
        self.assertFalse(task.completed)



class TaskAPITest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.task = Task.objects.create(title="Test Task", description="Test Desc")

    def test_get_task_list(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        data = {'title': 'New Task', 'description': 'Created via test'}
        response = self.client.post(reverse('task-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_update_task(self):
        data = {'title': 'Updated Task', 'description': 'Updated', 'completed': True}
        response = self.client.put(reverse('task-detail', args=[self.task.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')
        self.assertTrue(self.task.completed)

    def test_delete_task(self):
        response = self.client.delete(reverse('task-detail', args=[self.task.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)        
