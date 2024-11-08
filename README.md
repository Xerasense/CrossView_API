# CrossView REST API

## Overview

This is a Django REST API built to transfer data to the crossView mobile application and serve as the backend of the system. It is designed to handle data retrieval, user authentication, and image transfer, and is currently hosted on Railway.

## Features

- **Feature 1**: Perform CRUD operations on crossView database
- **Feature 2**: Make HTTP requests to port endpoint

## Technology Stack

- **Backend Framework**: Django
- **REST Framework**: Django REST Framework
- **Database**: MySQL Hosted on Railway
- **Hosting Platform**: Railway
- **Language**: Python 3.11

## Getting Started

### Prerequisites

To run this project locally, ensure you have the following installed:

- Python 3.11
- pipenv (for managing virtual environments and dependencies)
- MySQL or MariaDB for accessing the database

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Xerasense/CrossView_API.git
   cd CrossView_API

2. **Set up and run virtual environment**:

    ```bash
   pipenv install
   pipenv shell

3. **Install dependencies**:

    ```bash
   pip install -r requirements.txt
   
4. **Run the server (local)**:

    ```bash
   python manage.py runserver

## Optional

**How to create migrations**:
```bash
python manage.py makemigrations 
```

**How to apply migrations**:
```bash
python manage.py migrate
```
