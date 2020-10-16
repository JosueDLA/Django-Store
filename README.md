# Django Store

Store application with CRUD funtionality, API and authenitcation.

## Instalation

Clone this repository 

```bash
git clone https://github.com/JosueDLA/Django-Store
```

Install requirements.txt

```bash
pip install requirements.txt
```

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

## Commands

### Start Server

```sh
> python manage.py runserver
```

### Migrations

Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.

You should think of migrations as a version control system for your database schema. 

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

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.