del db.sqlite3
echo "Removed db.sqlite3"
py manage.py makemigrations
py manage.py migrate
py populate_dogs.py
