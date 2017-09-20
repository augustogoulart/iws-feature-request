import os
from decouple import config


BASEDIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = config('DEBUG')

HOST = config('HOST')

PORT = config('PORT')

SQLALCHEMY_ECHO = False

SQLALCHEMY_TRACK_MODIFICATIONS = True

SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(config('DB_USER'),
                                                                                        config('DB_PASS'),
                                                                                        config('DB_PORT'),
                                                                                        config('DB_NAME'))

SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, 'db_repository')


