# Django Blog Application

This is a simple blog application built with Django and Django REST Framework. The application allows users to create, retrieve, update, and delete blog posts. It also supports user registration and authentication using JWT.

## Features

- User registration and authentication
- Create, retrieve, update, and delete blog posts
- Add comments to blog posts
- Token authentication for secure API access

## Requirements

- Python 3.x
- Django 3.x or 4.x
- Django REST Framework
- Django REST Framework Authtoken

## Installation

1. **Clone the repository:**

    ```bash
    git clone <(https://github.com/Subhinpreet03/blog)>
    cd <repository-directory>
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install django djangorestframework djangorestframework authtoken
    ```

4. **Create and configure the Django project:**

    ```bash
    django-admin startproject blog_project
    cd blog_project
    django-admin startapp blog
    ```
