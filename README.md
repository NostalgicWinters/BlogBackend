# Blog Backend

A modern backend for a blog application built with **FastAPI**. This project provides a REST API for managing blog posts, users, authentication, and other blog-related features. The project is currently under active development.

## Features

* FastAPI-powered REST API
* User authentication
* Blog post management
* Database integration
* Modular project structure
* Automatic API documentation
* Request validation using Pydantic
* Async support

> **Note:** This project is under active development. Features and API endpoints may change.

---

## Tech Stack

* **Framework:** FastAPI
* **Language:** Python
* **Validation:** Pydantic
* **ASGI Server:** Uvicorn

Additional technologies such as the database, ORM, and authentication library will be documented as development progresses.

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/NostalgicWinters/BlogBackend.git
cd BlogBackend
```

### Create a Virtual Environment

**Linux/macOS**

```bash
python -m venv .venv
source .venv/bin/activate
```

**Windows**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Development Server

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates interactive API documentation.

* Swagger UI:

  ```
  http://127.0.0.1:8000/docs
  ```

* ReDoc:

  ```
  http://127.0.0.1:8000/redoc
  ```

---

*The structure may evolve as the project grows.*

---

## Roadmap

* [ ] User registration
* [ ] User authentication
* [ ] JWT authorization
* [ ] CRUD operations for blog posts
* [ ] Comments
* [ ] Tags and categories
* [ ] Image uploads
* [ ] Pagination
* [ ] Search functionality
* [ ] Unit and integration tests
* [ ] Docker support
* [ ] CI/CD pipeline

---

## Contributing

Contributions, suggestions, and issue reports are welcome. Feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License.

---

## Status

🚧 **Work in Progress**

This backend is actively being developed. Expect breaking changes as new features are added and the architecture evolves.
