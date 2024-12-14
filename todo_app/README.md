To-Do Application

A simple To-Do application built with Django, designed to help users manage tasks. The project focuses on backend development and exposes basic APIs.

Features

Task Management:

Add, edit, and delete tasks.

Mark tasks as complete or pending.

Tagging System:

Categorize tasks with tags.

Reuse tags across multiple tasks.

Due Date Tracking:

Set deadlines for tasks.

View overdue tasks.

REST API Support:

Basic CRUD operations for tasks and tags.

Tech Stack

Backend: Django (with Django Rest Framework for APIs)

Database: Configured using the Django admin interface (MySql)

Installation

1. Clone the repository:
git clone https://github.com/Adarsh203-cmd/ToDoApp.git
cd todo-app

2. d activate it: venv\Scripts\activate

3. Install dependencies: pip install -r requirements.txt

4. Apply migrations: python manage.py migrate

5. Run the development server: python manage.py runserver

6. Access the application at http://127.0.0.1:8000/admin

superuser:  username: admin
            password: admin@123

7. user postman for testing:
      
      http://127.0.0.1:8000.

Project Structure

├── todo_app
│   ├── settings.py      # Project settings
│   ├── urls.py          # URL routing
│   ├── models.py        # Database models
│   ├── views.py         # View logic
│   ├── serializers.py   # DRF serializers
│   └── tests.py         # Unit tests
├── requirements.txt     # Python dependencies
├── manage.py            # Django management script
└── README.md            # Project documentation

REST API Endpoints

The following are the intended API endpoints. If discrepancies are found, verify them within the urls.py file.

Method

Endpoint

Description

GET

/api/todoitems/

List all tasks

POST

/api/todoitems/

Create a new task

GET

/api/todoitems/{id}/

Retrieve a specific task

PUT

/api/todoitems/{id}/

Update a specific task

DELETE

/api/todoitems/{id}/

Delete a specific task

Tests

Run unit tests: python manage.py test


