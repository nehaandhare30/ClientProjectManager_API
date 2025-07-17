# ClientProjectManager_API
This is a Django REST API built for managing clients and their associated project data. It uses MySQL as the database backend and follows best practices for modular design and RESTful API development.

🚀 Features
CRUD operations for client management

MySQL as the relational database

Django REST Framework for API endpoints

Admin interface for backend data control

Scalable, modular architecture


🛠 Tech Stack
Python 3.10+

Django 4.x

Django REST Framework

MySQL 5.7/8.0+

📦 Installation & Setup
1. Clone the Repository
git clone https://github.com/your-username/clientProjectManager_API.git
cd clientProjectManager_API

2. Create & Activate Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

4. Install Dependencies
pip install -r requirements.txt

If requirements.txt is missing:
pip install django
pip install djangorestframework
pip install mysqlclient

5. Configure MySQL Database
Edit settings.py and update the DATABASES section:
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

6. Run Migrations
python manage.py makemigrations
python manage.py migrate

7. Create Superuser
python manage.py createsuperuser

8. Run the Development Server
python manage.py runserver

Visit the API at:
http://127.0.0.1:8000/
Admin Panel:
http://127.0.0.1:8000/admin/
