# Rate My Dog &middot;
> University of Glasgow Computing Science Web Application Development Group Project

Rate My Dog is a Django based web application that facilitates user ratings on a database of dog images. By crowdsourcing ratings, the site finds and reports the top rated dogs.

## Installing / Getting started

Python 3.5 or greater is required.

```shell
pip3 install -r requirements.txt
python3 ratemydog/manage.py runserver
```

These commands will install all the required python modules and begin the Django webserver.

## Developing

### Built With
Bootstrap CSS, jQuery, Popper.js,

### Prerequisites
https://www.python.org/downloads/

## Tests

### Running Tests
```shell
python manage.py test
```
### Testing Code Coverage
Running tests:
```shell
coverage run --source='.' manage.py test
```
Viewing report:
```shell
coverage report
```
### User testing

Populate.py creates SUPERUSER::123, TESTUSER::123, NEWUSER::123 which can be used to login for testing purposes although signing up is functional.

## Style guide

[Pep8](https://www.python.org/dev/peps/pep-0008/)


## Database

SQLite 
