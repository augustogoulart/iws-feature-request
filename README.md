# IWS Feature Request App

[![Build Status](https://travis-ci.org/augustogoulart/iws-feature-request.svg?branch=master)](https://travis-ci.org/augustogoulart/iws-feature-request)

### This is not the first release yet!
Up to this moment, the app is running on an AWS EC2 instance at:

http://ec2-54-245-49-5.us-west-2.compute.amazonaws.com

At this point we have a Flask application serving a static page that contains the app layout and The API is starting taking shape.
for better visualization, I'd recommend this Chrome extension: [JSON Viewer](https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh?utm_source=chrome-app-launcher-info-dialog
)

**Feature requests list:**

**_GET_** /api/requests/

**Feature request detail:**

**_GET_** /api/requests/1

**Adding a feature:**

**_POST_** /api/requests/ title='title',client='client', description='description', target_date='yyy-mm-dd'

Obs: If a client does not exits, it will be automatically created.

**Clients list:**

**_GET_** /api/clients/

**Client detail:**

**_GET_** /api/clients/1

**Client post:**

_**POST**_  /api/clients/ name='name'

## TODO
Front end integration


### Running locally 
**1. Clone the repo:**
``` 
git clone https://github.com/augustogoulart/iws-feature-request
```
**2. Access the project root:**
```
cd iws-feature-request
```
**3. Create a virtual enviroment: (python 3.6+)**
```
python -m venv .venv
```
**4. Activate the virtual enviroment:**
```
source .venv/bin/activate
```
**5. Run the setup script:**
```
make setup
```
**6. Install the test requirements:**
```
make setup-test
```
**7. Run the tests:**
```
make test
```
**8. Run the project:**
```
make run
```
**9. See the project live at:**
```
http://localhost:5000/
```
