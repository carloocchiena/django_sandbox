- update requirements.txt: `pip list --format=freeze > requirements.txt`

- start django app: `django-admin startproject my_project`

- run django server: `python manage.py runserver -port=8000`

- start new django app: `python manage.py startapp my_app`

- migrate the main database: `python manage.py migrate`

- migrate the app database: `python manage.py migrate my_app`

- see SQL commands run by django: `python manage.py sqlmigrate first_app 0001`

- run django shell: `python manage.py shell`
