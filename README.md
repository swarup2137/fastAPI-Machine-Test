# FastAPI Machine Test

This project is a backend system built using FastAPI to manage users, clients, and projects. It was developed as part of a machine test to demonstrate API design, database relationships, and backend development skills.

---

## Overview

The system supports:

* User registration and login
* Client creation and management
* Project creation and assignment

Each client can have multiple projects, and each project can be assigned to multiple users.

---

## Tech Stack

* FastAPI
* MySQL
* SQLAlchemy
* Pydantic
* Uvicorn

---

## Project Structure

app/

* main.py
* database.py
* models.py
* schemas.py
* auth.py
* dependencies.py
* routers/

  * user.py
  * client.py
  * project.py

---

## Setup Instructions

### 1. Clone the repository

git clone https://github.com/swarup2137/fastAPI-Machine-Test.git
cd fastAPI-Machine-Test

### 2. Create virtual environment

python -m venv venv
venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

---

## Database Setup

Make sure MySQL is installed and running.

Create database:
CREATE DATABASE fastapi_db;

Update connection in `app/database.py`:
DATABASE_URL = "mysql+pymysql://root:yourpassword@localhost/fastapi_db"

---

## Run the Application

uvicorn app.main:app --reload

Open browser:
http://127.0.0.1:8000/docs

---

## API Testing Flow

1. Register user → /users/
2. Login → /auth/login
3. Create client → /clients/
4. Create project → /projects/
5. Fetch data → /clients/ and /projects/

---

## Features

* RESTful API design
* User, Client, Project management
* Many-to-many relationship (User ↔ Project)
* One-to-many relationship (Client → Project)
* Input validation and error handling

---

## Notes

* JWT token generation is implemented (basic)
* Passwords are stored as plain text (can be improved)
* This project is built for learning and demonstration purposes

---

## Author

Swarup Raut
