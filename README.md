# IIITV OC Backend
This is the API for IIITV Online Campus project.

### To install:

##### Step 1: Create a virtual env
```sh
virtualenv venv
```

##### Step 2: Install requirements
```sh
pip3 install -r requirements.txt
```

### Database migrations:

##### Step 1: Create migrations
```sh
python manage.py makemigrations
```

##### Step 2: Migrate the created migrations
```sh
python manage.py migrate
```

### Run the server:

```sh
python manage.py runserver
```