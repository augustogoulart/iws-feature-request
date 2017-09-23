setup:
		pip install --upgrade -r requirements/requirements.txt

setup-test:
	    pip install --upgrade -r requirements/test.txt

test:
	    nose2 -v --with-coverage

run:
	    python wsgi.py

gunicorn:
	    gunicorn --bind 0.0.0.0:80 --workers=4 wsgi:app

