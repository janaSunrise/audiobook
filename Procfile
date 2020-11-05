release: python manage.py makemigrations && python manage.py migrate
web: gunicorn base.wsgi --log-file - 