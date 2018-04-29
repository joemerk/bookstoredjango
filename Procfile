web: gunicorn mystore.wsgi --log-file -
release: python manage.py migrate
heroku config:set DISABLE_COLLECTSTATIC=1
python manage.py collectstatic --noinput