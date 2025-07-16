# 🎓 Student Portal - Django + MySQL

A complete Student Management System built with Django and MySQL. Includes login system, CRUD operations, profile image upload, Bootstrap UI, and more.

## 🔧 Features

- ✅ User Authentication (Login/Logout)
- ✅ Add, Edit, Delete Student Records
- ✅ Upload Profile Image
- ✅ Email, Phone, and Address Details
- ✅ Search by Name or Class
- ✅ Flash Messages (Login Success, Errors)
- ✅ Responsive Bootstrap Design
- ✅ Pagination for student list
- ✅ Created with MySQL as backend DB

## 🛠️ Tech Stack

- **Backend:** Python (Django 5.2)
- **Database:** MySQL
- **Frontend:** HTML, CSS, Bootstrap
- **Other Tools:** Django Messages Framework, MySQL Workbench

## 🚀 How to Run Locally

```bash
git clone https://github.com/PavanBommidi07/student-portal.git
cd student-portal

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start server
python manage.py runserver
