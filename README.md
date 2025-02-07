# DA-ETSISI Feedback Platform

## Introduction

The **DA-ETSISI Feedback Platform** is a web application designed to collect and manage feedback from students at ETSISI. The platform allows users to submit their opinions and suggestions to improve academic and extracurricular aspects of the school.  

Built with **Django**, the application provides a secure and user-friendly interface to ensure seamless interaction. It is also containerized with **Docker**, making deployment and database management efficient.  

---

## 1. Configuration Changes in `settings.py`

To ensure proper functionality, the following modifications are required in `settings.py`:

### 1.1 Remove `_c` from a Variable Name

Find the relevant variable in `settings.py` that includes `_c` in its name and rename it by removing `_c`.

### 1.2 Add a Required Key

A specific key (provided separately) must be added to `settings.py` to enable the application to function correctly.

---

## 2. MariaDB Compatibility in Docker

The provided **Dockerfile** ensures compatibility with **MariaDB**. To configure the database correctly, update `settings.py` with the appropriate **DATABASES** settings.

### 2.1 Updating `settings.py` for MariaDB

Modify the `DATABASES` section in `settings.py` as follows:

``` python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": "database",
        "PORT": port,
        "PASSWORD": "contraseña",
        "USER": "user",
        "NAME": "name",
  }
```
### 2.2 Explanation of Parameters

- **ENGINE**: Uses the MySQL backend (`django.db.backends.mysql`), which is compatible with MariaDB.
- **HOST**: The service name of the database container (e.g., `"database"`).
- **PORT**: The port number for the MariaDB server.
- **PASSWORD**: The password for the database user.
- **USER**: The database username.
- **NAME**: The name of the database.

### 2.3 Additional Database Considerations

- If using an **external MariaDB instance**, replace `"database"` in `HOST` with the actual server address.
- Ensure that **MariaDB is running** before starting the Django application.
- You may need to **install MySQL client dependencies**:

  ```sh
  pip install mysqlclient

## 3. Running the Application

### 3.1 Running with Docker

Once the necessary modifications are made, build and run the application using:

```sh
docker-compose up --build
```

This command will:

- Build the **Django application** and its dependencies.
- Set up a **MariaDB database container**.
- Launch both services, allowing the application to interact with the database.

### 3.2 Running Without Docker

If running without Docker, ensure MariaDB is installed and configured, then start the Django development server:

```sh
python manage.py runserver
```

## 4. Additional Notes

- **Check your `.env` file**: Ensure database credentials are correctly set.
- **Apply migrations**: 

```sh
  python manage.py migrate
```
- **Create a superuser** (optional):

```sh
  python manage.py createsuperuser
```

- **Access the application** at [http://localhost:8000](http://localhost:8000).
- **Restart the application** after modifying `settings.py`.

For debugging, check logs using:

``` sh
docker-compose logs -f
```