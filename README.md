# To-Do Application

A simple To-Do application built with Django, designed to help users manage tasks. The project focuses on backend development and exposes basic APIs.

## Features

- **Task Management**:
  - Add, edit, and delete tasks.
  - Mark tasks as complete or pending.
- **Tagging System**:
  - Categorize tasks with tags.
  - Reuse tags across multiple tasks.
- **Due Date Tracking**:
  - Set deadlines for tasks.
  - View overdue tasks.
- **REST API Support**:
  - Basic CRUD operations for tasks and tags.

## Tech Stack

- **Backend**: Django (with Django Rest Framework for APIs)
- **Database**: Configured using the Django admin interface (MySQL)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Adarsh203-cmd/ToDoApp.git
   cd todo-app
   
2. Activate the virtual environment:
   ```bash
   env\Scripts\activate

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Apply migrations:
   ```bash
   python manage.py migrate

5. Run the development server:
   ```bash
   python manage.py runserver

## Access teh application at http://127.0.0.1:8000/admin
  - ##superuser credentials:
  - username: admin
  - password: admin@123

 6. Use Postman for API testing: http://127.0.0.1:8000/api/todoitems/

## REST API Endpoints
 The following are the intended API endpoints. If discrepancies are found, verify them within the urls.py file.
 
| Method | Endpoint             | Description              |
| ------ | -------------------- | ------------------------ |
| GET    | `/api/todoitems/`    | List all tasks           |
| POST   | `/api/todoitems/`    | Create a new task        |
| GET    | `/api/todoitems/{id}/` | Retrieve a specific task |
| PUT    | `/api/todoitems/{id}/` | Update a specific task   |
| DELETE | `/api/todoitems/{id}/` | Delete a specific task   |


## Tests
-Run unit tests:
   ```bash
     python manage.py test
