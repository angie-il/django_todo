from django.test import TestCase
from .models import Task

# Create your tests here.
class TaskModelTestCase(TestCase):
    def setUp(self):
        self.task1 = Task.objects.create(
            title = 'Task 1',
            description = 'Description for task1',
            completed = False       
        )
        self.task2 = Task.objects.create(
            title='Task 2',
            description='Description for Task 2',
            completed=True
        )
        
    def test_task_creation(self):
        self.assertEqual(self.task1.title, 'Task 1')
        self.assertEqual(self.task2.description, 'Description for Task 2')
        self.assertTrue(self.task2.completed)
        
    def test_task_str(self):
        self.assertEqual(str(self.task1), 'Task 1')
    
    def test_task_update(self):
        self.task1.title = 'Updated Task 1'
        self.task1.save()
        updated_task = Task.objects.get(id=self.task1.id)
        self.assertEqual(updated_task.title, 'Updated Task 1')

    def test_task_deletion(self):
        task_count_before_delete = Task.objects.count()
        self.task2.delete()
        task_count_after_delete = Task.objects.count()
        self.assertEqual(task_count_after_delete, task_count_before_delete - 1)

    def test_task_defaults(self):
        new_task = Task.objects.create(title='New Task')
        self.assertFalse(new_task.completed)
