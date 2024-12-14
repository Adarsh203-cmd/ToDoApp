To-Do Application
A simple To-Do application built with Django, designed to help users manage their tasks effectively. This project focuses on backend development and exposes REST APIs for task management.

Features
Task Management:
Add, edit, and delete tasks.
Mark tasks as complete or pending.
Tagging System:
Categorize tasks with reusable tags.
Due Date Tracking:
Set deadlines for tasks.
View overdue tasks.
API Support:
Perform CRUD operations on tasks and tags using REST APIs.
Tech Stack
Backend: Django (using Django Rest Framework for API development).
Database: Configured using the Django admin interface (MySQL).
Installation
Follow these steps to set up and run the project locally:

Clone the repository:

bash
Copy code
git clone https://github.com/Adarsh203-cmd/ToDoApp.git
cd todo-app
Activate the virtual environment:

bash
Copy code
venv\Scripts\activate  # On Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations:

bash
Copy code
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
Access the application:

Admin interface: http://127.0.0.1:8000/admin
Credentials:
Username: admin
Password: admin@123
Test APIs using Postman:

Base URL: http://127.0.0.1:8000
Project Structure
plaintext
Copy code
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
The following endpoints are available for managing tasks. If discrepancies exist, refer to urls.py for accurate details.

Method	Endpoint	Description
GET	/api/todoitems/	List all tasks
POST	/api/todoitems/	Create a new task
GET	/api/todoitems/{id}/	Retrieve a specific task
PUT	/api/todoitems/{id}/	Update a specific task
DELETE	/api/todoitems/{id}/	Delete a specific task
Example API Request:
bash
Copy code
curl -X POST http://127.0.0.1:8000/api/todoitems/ \
     -H "Content-Type: application/json" \
     -d '{
       "title": "Complete the README",
       "description": "Finalize and polish the README content.",
       "due_date": "2024-12-31",
       "status": "pending"
     }'
Tests
Run unit tests using the following command:

bash
Copy code
python manage.py test
