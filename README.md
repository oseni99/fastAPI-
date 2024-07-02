# FastAPI Project README
## Introduction
 This project is built using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. This README provides an overview of the endpoints, the database setup, OAuth authentication, Pydantic models, schemas, and routers used in this project.
## Database
 The project uses SQLAlchemy as the ORM for interacting with the database. The database configuration is handled in database.py, where the database URL is fetched from environment variables for security.
 Run the FastAPI Application with Uvicorn:
 
**Run the development server:**
```sh
    fastapi dev main.py
```
 **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000/`
