# 🎯 To-Do List - Backend (FastAPI)

This is the server (API) for the To-Do List application. It was developed in Python using the **FastAPI** framework to manage task CRUD operations.

> **⚠️ Note on Persistence:** Currently, this API uses **volatile memory (RAM)** storage. This means that data is reset whenever the server restarts or enters sleep mode on Render (after 15 minutes of inactivity).

## 🚀 Technologies Used

* **Python 3.10+**
* **FastAPI**: Modern, high-performance framework.
* **Uvicorn/Gunicorn**: ASGI servers for production.
* **Pydantic**: For data validation and schemas.
* **CORS Middleware**: Configured to allow frontend access.

## 🛠️ Features

* `GET /tasks`: Lists all tasks.
* `POST /tasks`: Creates a new task.
* `PUT /tasks/{id}`: Updates title, description, or status of an existing task.
* `DELETE /tasks/{id}`: Removes a task from the list.

## 📥 How to run the project locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/joaopedro08-dev/todolist-backend.git](https://github.com/joaopedro08-dev/todolist-backend.git)
   cd todolist-backend
2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Linux/Mac:
   source .venv/bin/activate
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Start the server:**
   ```bash
   uvicorn main:app --reload
### The API will be available at http://127.0.0.1:8000. You can access the interactive documentation (Swagger) at http://127.0.0.1:8000/docs.

🔗 Live API Endpoint
You can access the live backend at:

https://todolist-backend-zxq2.onrender.com/tasks

## 🌐 Deploy on Render

The deployment was performed on **Render**. Since this application uses in-memory storage, it is crucial to run it as a single process to maintain data consistency across requests. 

The following **Start Command** was configured in the Render Dashboard:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
