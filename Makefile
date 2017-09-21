setup:
		pip install --upgrade -r requirements/requirements.txt
        export FLASK_APP=iws_feature_request/wsgi.py
setup-test:
	    pip install --upgrade -r requirements/test.txt

test:
	    py.test --cov iws_feature_request/tests

run:
	    cd iws_feature_request && python wsgi.py

gunicorn:
	    cd iws_feature_request && gunicorn --bind 0.0.0.0:5000 --workers=3 wsgi:app
