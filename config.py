# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_ECHO=False

#your email configuration
SMTP_SERVER = ''
PORT = 0
SERVER_LOGIN = ''
SERVER_PASSWORD = ''
SENDER = ''
RECEIVERS = [] #must be a list
SUBJECT = ''

MAX_PRICE = 0
CITY = ''
