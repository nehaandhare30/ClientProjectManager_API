# Client Project Manager API

A robust Django REST API for managing clients and their project data, built with Django REST Framework and MySQL.

---

## Overview

Client Project Manager API is a backend service that enables structured client and project management. It supports authenticated operations for both admin and client-specific access levels. The application includes full CRUD operations, automatic slug generation for clean URLs, and user-project assignments.

---

## Features

- CRUD operations for clients
- Nested project creation under clients
- User-based project visibility
- Slug-based URL support
- MySQL database integration
- Django admin panel for backend management

---

## Tech Stack

- **Language:** Python 3.10+  
- **Framework:** Django 4.x  
- **API:** Django REST Framework  
- **Database:** MySQL  
- **Admin Panel:** Django Admin  
- **Tools:** pip, venv, mysqlclient

---

## Project Setup

### Clone the Repository
git clone https://github.com/nehaandhare30/ClientProjectManager_API.git
cd ClientProjectManager_API

### Create and Activate a Virtual Environment
python3 -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate

### Install Dependencies
pip install -r requirements.txt

If requirements.txt is not available:
pip install django 
pip install djangorestframework 
pip install mysqlclient

### MySQL Database Configuration
Update settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

### Run Migrations and Start Server
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

---

## Accessing the Application

After running the server, you can access:

- **Admin Interface**  
  Navigate to: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)  
  Use your superuser credentials to log in and manage clients, projects, and users through Django's admin panel.

- **API Root**  
  Navigate to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
  This is the entry point for exploring and interacting with the API using tools like Postman or through a browsable web API.

---

## API Endpoints

### Client Endpoints

| Method | Endpoint         | Description                                      |
|--------|------------------|--------------------------------------------------|
| GET    | `/clients/`      | List all clients                                 |
| POST   | `/clients/`      | Create a new client                              |
| GET    | `/clients/:id/`  | Retrieve a client with its users' projects       |
| PUT    | `/clients/:id/`  | Update a client's information                    |
| DELETE | `/clients/:id/`  | Delete a client                                  |

### Project Endpoints

| Method | Endpoint                    | Description                                           |
|--------|-----------------------------|-------------------------------------------------------|
| POST   | `/clients/:id/projects/`    | Create a new project for a specific client            |
| GET    | `/projects/`                | List all projects assigned to the logged-in user      |

> Note: `:id` refers to the client ID.

---

## Example Requests
### Create Project for a Client

POST /clients/1/projects/
Content-Type: application/json

{
  "project_name": "Website Redesign",
  "users": [1]
}
> Note: Here users indicate the admin user id which is created by createsuperuser.

---

## Project Structure

ClientProjectManager_API/
├── clientapp/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── clientProjectManager_API/
│   ├── settings.py
│   └── urls.py
├── manage.py


---

### License
This project is licensed under the MIT License.
