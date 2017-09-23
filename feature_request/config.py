import os

from decouple import config

BASEDIR = os.path.abspath(os.path.dirname(__file__))

DB_USER = config('DB_USER')

DB_PASS = config('DB_PASS')

DB_PORT = config('DB_PORT')

DB_NAME = config('DB_NAME')

DEBUG = config('DEBUG', default=True, cast=bool)

HOST = config('HOST')

PORT = config('PORT', cast=int)

SQLALCHEMY_ECHO = False

SQLALCHEMY_TRACK_MODIFICATIONS = True

SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_PORT}/{DB_NAME}"

SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, 'db_repository')
