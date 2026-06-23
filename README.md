# Task Management API 🚀

A REST API built using FastAPI for managing users and tasks with JWT Authentication.

This project is created to practice backend development using FastAPI, SQLAlchemy, PostgreSQL and Alembic.

> Screenshots are captured using dummy test data.

---

## Features ✨

## User Features

- User Registration
- User Login
- Password Hashing
- JWT Token Generation
- User Authorization


## Task Features

- Create Task
- Get All Tasks
- Get Task By ID
- Update Task
- Delete Task
- User based task management


## Database Features

- PostgreSQL Database
- SQLAlchemy ORM
- Alembic Migration
- User and Task One-To-Many Relationship


---

## Tech Stack 🛠️

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic
- JWT
- Passlib


---

## Project Structure 📂

 ```text

task_management_API
│
├── src
│ │
│ ├── users
│ │ ├── models.py
│ │ ├── routes.py
│ │ ├── controller.py
│ │ └── schemas.py
│ │
│ ├── tasks
│ │ ├── models.py
│ │ ├── routes.py
│ │ ├── controller.py
│ │ └── schemas.py
│ │
│ └── utils
│ ├── db.py
│ ├── settings.py
│ └── helper.py
│
├── migrations
├── main.py
├── requirements.txt
└── README.md
```
---
# API Documentation 📖

Swagger Documentation:


http://127.0.0.1:8000/docs

---

# Swagger Screenshots

## User Registration

<img width="1913" height="983" alt="Screenshot (323)" src="https://github.com/user-attachments/assets/979b7a98-47ee-43c5-8b71-ad1e69019626" />




## Task API

<img width="1852" height="921" alt="Screenshot (320)" src="https://github.com/user-attachments/assets/8a672ed9-df98-4e0f-97da-6659e1dac656" />



## Authentication

<img width="1887" height="972" alt="Screenshot (324)" src="https://github.com/user-attachments/assets/2a6400f4-e78f-4585-ba2c-925863544edd" />

---

 # Installation ⚙️

## 1. Clone Repository

https://github.com/pratikdevbuilds/task_management_API


## 2. Go inside project folder

cd task_management_API


## 3. Create virtual environment

python -m venv env


## 4. Activate virtual environment

Windows:

env\Scripts\activate


## 5. Install dependencies

pip install -r requirements.txt


## 6. Create .env file

Example:

DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256


## 7. Run database migration

alembic upgrade head


## 8. Start server

uvicorn main:app --reload
 
Now open:

http://127.0.0.1:8000/docs
