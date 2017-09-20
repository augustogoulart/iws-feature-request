setup:
		pip install --upgrade -r requirements/requirements.txt
        export FLASK_APP=iws_feature_request/app.py
setup-test:
	    pip install --upgrade -r requirements/test.txt

test:
	    py.test --cov iws_feature_request/tests

run:
	    flask run
