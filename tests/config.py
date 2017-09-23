import os
from decouple import config


TEST_DB_USER = config('TEST_DB_USER')

TEST_DB_PASS = config('TEST_DB_PASS')

TEST_DB_PORT = config('TEST_DB_PORT')

TEST_DB_NAME = config('TEST_DB_NAME')

BASEDIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = config('DEBUG', default=True, cast=bool)

HOST = config('TEST_HOST')

TESTING = True

PORT = config('TEST_PORT')

SERVER_NAME = config('SERVER_NAME')

WTF_CSRF_ENABLED = False

SQLALCHEMY_ECHO = False

SQLALCHEMY_TRACK_MODIFICATIONS = True

SQLALCHEMY_DATABASE_URI = f"postgresql://{TEST_DB_USER}:{TEST_DB_PASS}@{TEST_DB_PORT}/{TEST_DB_NAME}"

SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, 'db_repository')
