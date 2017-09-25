setup:
	    @cd feature_request && export FLASK_APP=wsgi.py
		@pip install --upgrade -r requirements/requirements.txt

setup-test:
	    @pip install --upgrade -r requirements/test.txt

test:
	    @nose2
		@coverage report -i -m

run:
	    @cd feature_request && export FLASK_DEBUG=1 && flask run

migrate:
		@cd feature_request && flask db migrate

upgrade:
	    @cd feature_request && flask db upgrade

gunicorn:
	    gunicorn --bind 0.0.0.0:80 --workers=4 feature_request.wsgi:app

