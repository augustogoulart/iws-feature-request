# IWS Feature Request App

[![Build Status](https://travis-ci.org/augustogoulart/iws-feature-request.svg?branch=master)](https://travis-ci.org/augustogoulart/iws-feature-request)

### This is not the first release yet!
Up to this moment, the app is running on an AWS EC2 instance at:

http://ec2-54-191-66-93.us-west-2.compute.amazonaws.com:5000

At this point we have a Flask application serving a static page that contains the app layout and The API is starting taking shape.
for better visualization, I'd recommend this Chrome extension: [JSON Viewer](https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh?utm_source=chrome-app-launcher-info-dialog
)

**Feature requests list:**

**_GET_** :5000/api/requests/

**Feature request detail:**

**_GET_** :5000/api/requests/1

**Adding a feature:**

**_POST_** :5000/api/requests/ title='title',client='client', description='description', target_date='yyy-mm-dd'

Obs: If a client does not exits, it will be automatically created.

**Clients list:**

**_GET_** :5000/api/clients/

**Client detail:**

**_GET_** :5000/api/clients/1

**Client post:**

_**POST**_ :5000/api/clients/ name='name'

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
**3. Create a virtual enviroment: (python 3.5+)**
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
