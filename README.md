#FastAPi Todo Aplication

This is a simple FastAPI project created as a learning and portfolio application. The main goal of this project was to understand how backend applications work in practice: authentication, working with database, routing, and basic frontend integration.

Implemented features:
- User registration and login
- Authentication using JWT stored in cookies
- Role-based access (admin and user)
- CRUDoperations for todo items
- HTML pages rendered with Jinja2
- Static files (CSS and JS)
- SQLAlchemy ORM
- Alembic migrations

Technologies used:
Python
FastAPI
SQLAlchemy
Alembic
Jinja2
SQLite

Project structure:
The main application code is located inside the TodoApp derictory. It contains routers, templates, static files, database configuration, and models. Alembic is used for Database migrations.

How to run locally:
Clone the repository and go to the project directory:
git clone
https://github.com/Maxle127/FastAPI.git
cd FastAPI
Install dependencies: pip install -r requirements.txt
Run the application: uvicorn TodoApp.main:app --reload
After that, open the browser and go to: https://127.0.0.1:8000

Notes:
SQLite is used for simplicity during development. The project can be extended and migrated to PostgreSQL in the future. This application is still evoling as i continue learning backend development.

Author
Maksym Leiza
Junior Python Backend Developer