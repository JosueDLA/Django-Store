# Django Store

Store Web App with Django

## Software and Tools Used
- Django
- Pipenv
- Bootstrap
- Pylint

Setup
**Django**
```sh
> pipenv install django
```

**Pylint**
```sh
> pipenv install pylint-django
```

## Overview 

TBD

## Commands

### Start Server

```sh
> python manage.py runserver
```

### Migrations

__makemigrations:__ _Create new migration based on hte changes yyou made on your model._
```sh
> python manage.py makemigrations
```

__migrate:__ _Responsable for applied/unapplied migrations._
```sh
> python manage.py migrate
```

__sqlmigrate :__ _Displays SQL statements for a migration_
```sh
> python manage.py sqlmigrate [App] [Migration ID]
```