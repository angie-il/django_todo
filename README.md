# Django To-Do List

A simple To-Do List application built with Django.

## Features

- Add, edit, and delete tasks
- Mark tasks as completed
- Responsive design using Bootstrap

## Usage
- Add Task: Click the "Add Task" button and fill in the form.
- Edit Task: Click the "Edit" button next to a task and update the details.
- Delete Task: Click the "Delete" button next to a task.
- Mark as Completed: The "Completed" badge will appear next to tasks that are marked as completed.

## Requirements

- Python 3.12.3
- Django 5.0.7
- Bootstrap 4.5.2

## Installation

1. Clone the repository:

```
git clone https://github.com/angie-il/django_todo.git
cd django_todo/todo_list
```

2. Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
3. Install Django

```
pip install django
```

4. Generate SECRET_KEY

```
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

5. Copy .env.example to .env and add the generated key to your .env 

```
cp .env.example .env

SECRET_KEY= 'GENERATED KEY'
``` 

6. Install the required packages:

```
pip install -r requirements.txt
```

7. Apply migrations:

```
python manage.py migrate
```

8. Run the development server:

```
python manage.py runserver
```

9. Open your web browser and go to http://localhost:8000.
