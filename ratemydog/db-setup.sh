#!/bin/bash

rm db.sqlite3
echo "Removed db.sqlite3"
python3 manage.py makemigrations
python3 manage.py migrate
python3 populate_dogs.py
