# Assets Tracking


## OVERVIEW
In this Django app to track corporate assets such as phones, tablets, laptops and other gears handed out to employees.

## GOALS

1. The application might be used by several companies
2. Each company might add all or some of its employees
3. Each company and its staff might delegate one or more devices to employees for a certain period of time
4. Each company should be able to see when a Device was checked out and returned
5. Each device should have a log of what condition it was handed out and returned


## Project Structure

```bash
.
└── assets-tracking/
    ├── config/                                     
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py                             # project settings
    │   ├── urls.py                                 # root URL
    │   └── wsgi.py
    ├── trackassets/                                # app name
    │   ├── api/                                    
    │   │   ├── permissions.py                      # custom permission
    │   │   ├── serializers.py                      # serializers 
    │   │   ├── urls.py                             # API ULS
    │   │   └── views.py                            # API views
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py                               # Django Models class
    │   ├── views.py
    │   └── tests.py
    ├── db.sqlite3                                  # Database 
    ├── manage.py
    ├── requirements.txt                            # project dependency
    └── Asset Tracking.postman_collection.json      # API documentation

```



## Installations Process for Windows

Install the virtual environment

    assets-tracking> python -m venv env

Activate the virtual environment (env)

    assets-tracking> env\Scripts\activate

Now, install the dependency inside the virtual environment

    (env) assets-tracking> pip install -r requirements.txt

After complete the installation, now run the server

    (env) assets-tracking> python manage.py runserver



## API Documentation include 
