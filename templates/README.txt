# Blog Application 

### Description
Simple Blog that manage user to login with username and password 
each user can add blog and modify its content or even delete it.

### Project Structure
```

│   db.sqlite3
│   manage.py
│   requirments.py
│
├───accounts
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───migrations
│   │   │   __init__.py
│   │   │
│   │   └───__pycache__
│   │           __init__.cpython-38.pyc
│   │
│   └───__pycache__
│           admin.cpython-38.pyc
│           models.cpython-38.pyc
│           urls.cpython-38.pyc
│           views.cpython-38.pyc
│           __init__.cpython-38.pyc
│
├───blog
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   tests.py
│   │   urls.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───migrations
│   │   │   0001_initial.py
│   │   │   __init__.py
│   │   │
│   │   └───__pycache__
│   │           0001_initial.cpython-38.pyc
│   │           __init__.cpython-38.pyc
│   │
│   └───__pycache__
│           admin.cpython-38.pyc
│           models.cpython-38.pyc
│           urls.cpython-38.pyc
│           views.cpython-38.pyc
│           __init__.cpython-38.pyc
│
├───blog_project
│   │   asgi.py
│   │   settings.py
│   │   urls.py
│   │   wsgi.py
│   │   __init__.py
│   │
│   └───__pycache__
│           settings.cpython-38.pyc
│           urls.cpython-38.pyc
│           wsgi.cpython-38.pyc
│           __init__.cpython-38.pyc
│
└───templates
    │   base.html
    │   home.html
    │   post_delete.html
    │   post_detail.html
    │   post_edit.html
    │   post_new.html
    │   signup.html
    │
    ├───learn scraping
    └───registration
            login.html

```


    
## Getting Started
### Pre-requisites and Local Development Server
* run pip install -r requirements.txt to install all packages and libraries needed for the project 

*run python manage.py makemigrations 
* run python manage.py migrate 
* run python manage.py runserver 
  
## The application is run at http://127.0.0.1:8000/
  
 

.
