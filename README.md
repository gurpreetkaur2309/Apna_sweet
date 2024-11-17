

---

# Apna Sweets

Welcome to the **Apna Sweet** repository! Follow the steps below to set up and run this project on your local machine.

---

## Features
- [Authentication,Authorization,Pagination,all Validation]

---

## Prerequisites

1. **Python**: Ensure you have Python 3.8+ installed. You can download it from [python.org](https://www.python.org/).
2. **Virtual Environment**: Recommended to isolate project dependencies.
3. **MySQL**: Ensure you have a MySQL server running for the database.

---

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/gurpreetkaur2309/Apna_sweet.git
cd Apna_sweet
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate    # On macOS/Linux
venv\Scripts\activate       # On Windows
```

### 3. Install Dependencies
Install all required Python packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Configure Database
1. Open `settings.py` in the `Apna_sweet` directory.
2. Update the `DATABASES` settings to match your MySQL configuration:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'Apna_sweets',
           'USER': 'root',
           'PASSWORD': 'root',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

### 5. Apply Migrations
Run the following commands to set up the database schema:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser
To access the admin panel, create a superuser:
```bash
python manage.py createsuperuser
```
Follow the prompts to set up a username, email, and password.

### 7. Run the Server
Start the Django development server:
```bash
python manage.py runserver
```

Access the project at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

---

## Usage

- **Admin Panel**: Visit `/admin` to manage the project backend.
- **Features**: Describe how to use key functionalities of your project.

---

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and create a pull request.

---

## License

[MIT License](LICENSE)

---
