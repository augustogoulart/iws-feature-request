# IWS Feature Request App

[![Build Status](https://travis-ci.org/augustogoulart/iws-feature-request.svg?branch=master)](https://travis-ci.org/augustogoulart/iws-feature-request)
[![Coverage Status](https://coveralls.io/repos/github/augustogoulart/iws-feature-request/badge.svg)](https://coveralls.io/github/augustogoulart/iws-feature-request)

#### The app is live at:

<del>http://ec2-54-218-77-21.us-west-2.compute.amazonaws.com/</del>
The app is not live anymore. 

## Methodology

**1.** The app was developed similarly as how I would develop an application for a client.

**2.** Since day-1 the app was live as a simple static page, so the client could check the progress.

**3.** If this were a real app I wouldn't say It's "done". This version would represent the stage where the client validate its first 
idea and send some feedback for me to make changes

## Stack
1. **Python 3.6.2** -  New features and improvements of the version were used, so backwards compatibility
is not guaranted.
2. **Flask** - Python micro framework requested.
3. **Flask-RESTful** - Flask extension to help building concise REST API's
4. **SQLAlchemy** - Database ORM
5. **PostgreSQL**: PostgresSQL is the only database used for development, production and CI. SQLAlchemy does a pretty good job as ORM, but it's "Mapping" 
nature is undeniable.So, to avoid inconsistencies the same database were used end-to-end.
6. **Boostrap V4 and Jquery** - For UI animations and responsiveness
7. **KnockoutJS** - Javascript library used for dynamic UI.


## Infrastructure
1. **AWS EC2:** The app is running on an AWS EC2 instance served by Gunicorn with 3 workers. Since the app is not
intended to support any heavier load, neither Nginx of Apache were used.
2. **Ubuntu 16.04 LTS:** The OS used is the Ubuntu 16.04 provided by AWS.
3. **Database**: The PostgresSQL production instance is running on the same machine.
4. **Static Files**: No service like AWS S3 or CDN is being used.



# Visualizing the API

For better visualization, I'd recommend this Chrome extension: [JSON Viewer](https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh?utm_source=chrome-app-launcher-info-dialog
)

**Feature requests list:**

**_GET_** /api/requests/

**Feature request detail:**

**_GET_** /api/requests/{id}

**Adding a feature request:**

**_POST_** /api/requests/ title='title' description='description' client='client' priority=1 target_date='2017-10-10' product_area='Billing'

_Obs: If a client does not exits, it will be automatically created._

**Deleting a feature request:**

**_DELETE_** /api/requests/{id}

**Patching a feature request:**

**_PATCH_** /api/requests/75 title='title' description='description' client='client' priority=1 target_date='2017-10-10' product_area='Billing'

# Running locally 
#### Creating the Database

**1. Install PostgreSQL:**
```
sudo apt-get install postgresql postgresql-contrib 
```

**2. Access PostgresSQL:**

```
sudo -iu postgres
```

**3. Create the Database:**

```
createdb requests
```

**4. Access the Database console:**
```
psql -d requests
```
**5. Create the user and grant access:**
```
CREATE ROLE britecore WITH LOGIN PASSWORD 'britecore';
GRANT ALL PRIVILEGES ON DATABASE requests TO britecore;
ALTER USER britecore CREATEDB;
```


#### Installing the application
**1. Clone the repo:**
``` 
git clone https://github.com/augustogoulart/iws-feature-request
```
**2. Access the project root:**
```
cd iws-feature-request
```

**3. Copy the sample environment file**
```
cp contrib/env-sample.txt .env
```
**4. Edit the .env file:**
```

DB_USER=britecore
DB_PASS=britecore
DB_PORT=127.0.0.1
DB_NAME=requests

```
**5. Create a virtual enviroment: (python 3.6+)**
```
python -m venv .venv
```
**6. Activate the virtual enviroment:**
```
source .venv/bin/activate
```

**6. Run the setup script:**
```
make setup
```
**6. Migrate the database**
```
make migrate
```

**7. Run the app:**
```
make run
```

**9. See the project live at:**
```
http://localhost:5000/
```

### Running the tests


**1. Access PostgresSQL:**

```
sudo -iu postgres
```

**3. Create the Database:**

```
createdb test_requests
```

**4. Access the Database console:**
```
psql -d requests
```
**5. Grant access:**
```
GRANT ALL PRIVILEGES ON DATABASE test_requests TO britecore;
```
**6. Install the tests requirements:**
```
make setup-test:

```
**7. Running the tests:**

```
make test
```



