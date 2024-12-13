from django.test import TestCase
from rest_framework.test import APITestCase
from .models import TodoItem, Tag
from rest_framework import status
from django.utils.timezone import now
from django.core.exceptions import ValidationError

class TodoModelTestCase(TestCase):

    def setUp(self):
        self.tag = Tag.objects.create(id="test-tag", name="Work")

    def test_todo_item_creation(self):
        """Test that a TodoItem is created successfully."""
        todo = TodoItem.objects.create(
            id="test-todo",
            title="Learn Django Testing",
            description="Complete the Django testing guide.",
            due_date=now().date(),
        )
        self.assertEqual(todo.status, 'OPEN')
        self.assertEqual(str(todo), "Learn Django Testing")

    def test_due_date_in_past(self):
        """Test that setting a past due_date raises a validation error."""
        with self.assertRaises(ValidationError):
            todo = TodoItem(
                id="test-todo",
                title="Invalid Todo",
                description="This should fail.",
                due_date=now().date().replace(year=now().year - 1),
            )
            todo.clean()

    def test_tag_creation(self):
        """Test that a Tag is created successfully."""
        self.assertEqual(str(self.tag), "Work")


class TodoIntegrationTestCase(APITestCase):

    def setUp(self):
        self.tag = Tag.objects.create(id="test-tag", name="Work")
        self.todo = TodoItem.objects.create(
            id="test-todo",
            title="Learn Django REST",
            description="Learn how to write integration tests.",
            due_date=now().date(),
        )
        self.todo.tags.add(self.tag)

    def test_get_todo_items(self):
        """Test fetching all Todo items."""
        response = self.client.get('/todoitems/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_todo_item(self):
        """Test creating a new Todo item."""
        data = {
            "id": "new-todo",
            "title": "New Todo",
            "description": "Integration test creation.",
            "due_date": now().date(),
            "tags": [self.tag.id],
        }
        response = self.client.post('/todoitems/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Todo")

    def test_mark_completed(self):
        """Test marking a Todo item as completed."""
        response = self.client.put(f'/todoitems/{self.todo.id}/mark_completed/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.status, 'COMPLETED')