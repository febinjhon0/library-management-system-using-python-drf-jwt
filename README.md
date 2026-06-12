# 📚 Library Management System

A full-stack **Library Management System** built using **Django, Django REST Framework (DRF), JWT Authentication, MySQL, HTML, and CSS**.

This project allows users to register, login, manage books and authors, and borrow/return books with full API support.

---

# 🚀 Features

## 🔐 Authentication
- User Registration
- User Login / Logout
- Session-based authentication (HTML)
- JWT Authentication (API)

---

## 📚 Book Management (CRUD)
- Add new books
- View all books
- Update book details
- Delete books
- Search books by title

---

## 👨‍🏫 Author Management (CRUD)
- Add authors
- View authors
- Update author details
- Delete authors

---

## 📖 Borrow System
- Borrow books (only if available)
- Return books
- Track borrowing history
- Prevent multiple borrowing of same book

---

## 🔗 Relationships
- One Author → Many Books
- One Book → Many Borrow Records
- One User → Many Borrow Transactions

---

## 🌐 REST API (DRF)
- Book APIs
- Author APIs
- Borrow APIs
- JWT Secure Authentication

---

## 🎨 Frontend (HTML + CSS)
- Login Page
- Registration Page
- Dashboard
- Books Listing Page
- Authors Listing Page
- Responsive UI design

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|--------|
| Django 3.2 | Backend Framework |
| Django REST Framework | API Development |
| SimpleJWT | Authentication |
| MySQL | Database |
| HTML | Frontend |
| CSS | Styling |
| Python | Programming Language |

---
# 📁 Project Structure


libraryManagementSystem/
│
├── library/
│ ├── migrations/
│ ├── templates/
│ │ └── library/
│ │ ├── login.html
│ │ ├── register.html
│ │ ├── dashboard.html
│ │ ├── books.html
│ │ ├── authors.html
│ │ └── add_book.html
│ │
│ ├── static/
│ │ └── css/
│ │ └── style.css
│ │
│ ├── models.py
│ ├── views.py
│ ├── api_views.py
│ ├── serializers.py
│ ├── urls.py
│
├── libraryManagementSystem/
│ ├── settings.py
│ ├── urls.py
│
├── manage.py
└── requirements.txt

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/library-management-system.git
cd library-management-system
2️⃣ Create Virtual Environment
python -m venv venv

Activate environment:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Configure MySQL Database

In settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'library_db',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
5️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate
6️⃣ Create Superuser
python manage.py createsuperuser
7️⃣ Run Server
python manage.py runserver

Open browser:

http://127.0.0.1:8000/
