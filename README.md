# django-library-tutorial
Simple library website built using Django framework


<!-- #### Screenshots -->

<!-- ![command_open](https://github.com/choia) -->

<!-- ![command_open](https://github.com/choia) -->

<!-- ![command_open](https://github.com/choia) -->

## Requirements

- Django 1.11.7
- Python 3.5.2
- PostgreSQL 9.5.10


## Procedure

Clone the repository first

- After that, virtualenv/virtualwrapper needs to be configured
- Once virtualwrapper is enabled in bashrc profile and virtualenv project has been created
```
    $ workon project-name 
    $ pip install -r requirements.txt
```

- Setup environmental variables in project postactivate script like below.
```
	export DJANGO_SETTINGS_MODULE=config.settings.local
	export PYTHONPATH=$PYTHONPATH:$HOME/Project/library-project/config
	export LOCAL_SECRET_KEY='YOURSECRETKEYHERE'
	export DATABASE_PASSWORD='DBPASS'
```

- Run makemigrations and then migration

```
	$ python manage.py makemigrations
    $ python manage.py migrate
```

- Run locally to test it out! Recommend logging into admin console first and add users, book, and author data for experiment.
<hr>

#### Library site Functionality

- Login/Logout authentication
- User with certain user group permission allows create, edit, and delete Author data & ability to renew the date of borrowed books for all borrowers
- Provide dynamic records of books, copies that are either available, on loan, reserved, and maintenance
- Pagination
- Test functionality to check the models, views, and templates

