# FastAPI Tasks API

![Python](https://img.shields.io/badge/python-3.x-blue)
![FastAPI](https://img.shields.io/badge/framework-FastAPI-green)
![Pytest](https://img.shields.io/badge/tested%20with-pytest-yellow)
![API](https://img.shields.io/badge/type-REST%20API-orange)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-blue)
![Status](https://img.shields.io/badge/build-passing-brightgreen)

Simple CRUD API for managing tasks, built with **FastAPI**.

This project demonstrates how I design a small backend service together with **automated tests and continuous integration**.

It showcases:

* REST API design
* automated testing using pytest
* FastAPI TestClient usage
* CI integration with GitHub Actions

---

# 🚀 Tech Stack

| Tool                       | Purpose                         |
| -------------------------- | ------------------------------- |
| Python 3.x                 | Programming language            |
| FastAPI                    | Web framework for building APIs |
| pytest                     | Testing framework               |
| FastAPI TestClient (httpx) | API testing client              |
| GitHub Actions             | Continuous Integration          |

---

# 📡 API Overview

The API exposes a minimal **task management system**.

### Available endpoints

| Method | Endpoint      | Description                |
| ------ | ------------- | -------------------------- |
| GET    | `/health`     | Basic healthcheck endpoint |
| GET    | `/tasks`      | Retrieve all tasks         |
| POST   | `/tasks`      | Create a new task          |
| GET    | `/tasks/{id}` | Retrieve a task by id      |
| PUT    | `/tasks/{id}` | Update an existing task    |
| DELETE | `/tasks/{id}` | Delete a task              |

---

# 🗂 Task Model

Each task contains the following fields:

| Field         | Type              | Description                        |
| ------------- | ----------------- | ---------------------------------- |
| `id`          | integer           | Task identifier                    |
| `title`       | string            | Short task title                   |
| `description` | string (optional) | Additional details                 |
| `done`        | boolean           | Indicates if the task is completed |

For simplicity this project uses **in-memory storage (Python list)**.
This is sufficient to demonstrate **API design patterns and automated testing**.

---

# 📁 Project Structure

```text
fastapi-tasks/

├── app/
│   ├── __init__.py
│   └── main.py              # FastAPI application and endpoints
│
├── tests/
│   ├── __init__.py
│   └── test_tasks_api.py    # API tests using TestClient
│
├── requirements.txt
├── pytest.ini
│
└── .github/
    └── workflows/
        └── tests.yml        # GitHub Actions workflow
```

### Directory overview

**app/**
Contains the FastAPI application and API endpoints.

**tests/**
Automated tests for API endpoints using pytest and FastAPI TestClient.

**requirements.txt**
Project dependencies.

**pytest.ini**
Pytest configuration.

**GitHub Actions workflow**
Continuous Integration pipeline configuration.

---

# ⚡ Running the API Locally

## 1. Clone the repository

```
git clone https://github.com/KacperBlok1/fastapi-tasks.git
cd fastapi-tasks
```

---

## 2. (Optional) Create a virtual environment

```
python -m venv venv
```

Activate it:

Windows

```
venv\Scripts\activate
```

Mac / Linux

```
source venv/bin/activate
```

---

## 3. Install dependencies

```
pip install -r requirements.txt
```

---

## 4. Start the FastAPI server

```
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

# 📚 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### OpenAPI schema

```
http://127.0.0.1:8000/openapi.json
```

These tools allow you to **test endpoints directly from the browser**.

---

# 🧪 Running Tests

The project includes a small but complete **automated test suite**.

Covered scenarios:

* API healthcheck
* creating tasks
* retrieving tasks
* updating tasks
* deleting tasks
* verifying `404` responses after deletion

Run all tests:

```
pytest
```

Tests use **FastAPI TestClient**, which allows testing the API without running an external server.

---

# 🔁 Continuous Integration

This repository includes a **GitHub Actions CI pipeline**.

Workflow location:

```
.github/workflows/tests.yml
```

### Pipeline steps

Triggered on:

* push
* pull_request to the `main` branch

Pipeline actions:

1. Sets up Python environment
2. Installs dependencies from `requirements.txt`
3. Runs the pytest test suite
4. Ensures the API behaves as expected

You can view the latest runs in the **Actions tab** of the repository.

---

# 🛠 Future Improvements

Possible improvements for the project:

* add persistent database (PostgreSQL or SQLite)
* add authentication (JWT)
* add pagination for tasks
* integrate API schema validation
* add Docker support

---

# 👨‍💻 Author

**Kacper Blok**

Backend / QA Automation Portfolio Project
