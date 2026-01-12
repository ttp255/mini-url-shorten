
  
# 📚 Mini url shortener

## 📝 Description

Modern, production-grade URL shortening service built with clean architecture  
and current best practices in mind.

## ✨ Features

- Shorten any long URL instantly  
- Clean, readable short codes (using shortuuid)  
- 307 Temporary Redirect    
- Simple, responsive frontend (no Tailwind, pure CSS)  
- Input validation & basic error handling  
- MongoDB storage with async Motor driver  
- Auto Swagger/OpenAPI documentation at `/docs`


## 📂 Project structure

    ├── mini-url-shortener/                   # Core application code
    │   ├── __init__.py
    │   │
    │   ├── main.py                 # FastAPI application entry point
    │   │                           # - Creates app instance
    │   │                           # - Mounts static files
    │   │                           # - Includes routers
    │   │                          
    │   ├── config.py               # Settings & environment variables management
    │   │                           # Uses pydantic-settings to load from .env
    │   │
    │   ├── database.py             # MongoDB connection management 
    │   │                           
    │   │
    │   ├── models/                 # Data models (mostly for MongoDB documents)
    │   │   └── url.py              # URLDocument model (Pydantic + MongoDB fields)
    │   │
    │   ├── schemas/                # Pydantic schemas for API/validation
    │   │   └── url.py              # URLCreate, URLPublic, etc.
    │   │
    │   ├── services/               # Business logic layer (should be most of your core logic)
    │   │   └── url_service.py      # Main logic: create short url, generate code,
    │   │                           # find by code, record click, etc.
    │   │
    │   └── routers/                # API/Web routes (FastAPI routers)
    │       └── url.py              # All endpoints:
    │                               #   - GET /           → home page
    │                               #   - POST /shorten   → create from form
    │                               #   - GET /{code}     → redirect
    │
    ├── templates/                  # Jinja2 HTML templates
    │   ├── base.html               # Common layout (head, styles, container)
    │   ├── index.html              # Main page with shorten form
    │   ├── success.html            # After successful shortening
    │   └── 404.html                # Custom not found page
    │
    ├── static/                     # Static files (CSS, JS, images...)
    │   └── css/
    │       └── style.css           # All styling (clean, modern, no Tailwind)
    │
    ├── .env                        # Environment variables (git ignored)
    │                               # MONGODB_URL, BASE_URL, etc.
    │
    ├── requirements.txt            # Project dependencies
    │
    ├── .gitignore                  # Standard python + env + pycache ignores
    │
    └── README.md                   # Project documentation
    |___ uv.lock                    # Lock dependencies   

## 🛠️ Prerequisites

Ensure you have the following installed:

* **Python 3.11+**
* **pip**
* **uv (package manager)**: 
    ```bash
    pip install uv # On Windows
    curl -LsSf https://astral.sh/uv/0.8.24/install.sh | sh # On Mac/Linux
    ```


## 💻 Installation

1.  **Clone the repository:**
    ```bash
    https://github.com/ttp255/mini-url-shorten.git
    cd mini-url-shorten
    ```

2.  **Create, activate a virtual environment and install dependencies:**
    ```bash  
    uv sync
    ```



3.  **Set up environment variables:**
    Create a file named `.env` in the root directory and add your necessary keys.

    ```
    
    MONGODB_URI=your_mongo_uri

    ```

## 🚀 Usage

### 1. Run the API Server
Start the FastAPI application
```bash
uv run uvicorn main:app
```
### 2. Access API Documentation
Visit your browser to see the interactive documentation:

* Swagger UI: http://localhost:8000/docs

* ReDoc: http://localhost:8000/redoc

## 🌐 API Endpoints

| Endpoint | Method | Description 
| :--- | :--- | :--- | 
| `/` | `GET` | Get home page.|
| `/{shor_code}` | `GET` | Redirect original link by short_code created.| 
| `/` | `POST` | Creat short code.|


