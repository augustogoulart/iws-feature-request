setup:
	    @cd feature_request && export FLASK_APP=wsgi.py
		@pip install --upgrade -r requirements/requirements.txt

setup-test:
	    @pip install --upgrade -r requirements/test.txt

test:
	    @nose2 --with-cov
		@coverage report -i -m

run:
	    @cd feature_request && export FLASK_DEBUG=1 && export FLASK_APP=wsgi.py && flask run

migrate:
		@cd feature_request && export FLASK_APP=wsgi.py && flask db migrate

upgrade:
	    @cd feature_request && export FLASK_APP=wsgi.py && flask db upgrade

gunicorn:
	    gunicorn --bind 0.0.0.0:80 --workers=3 feature_request.wsgi:app

