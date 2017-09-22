setup:
		pip install --upgrade -r requirements/requirements.txt
        export FLASK_APP=feature_request/wsgi.py
setup-test:
	    pip install --upgrade -r requirements/test.txt

test:
	    py.test --cov feature_request/tests

run:
	    cd feature_request && python wsgi.py

gunicorn:
	    cd feature_request && gunicorn --bind 0.0.0.0:80 --workers=3 wsgi:app
