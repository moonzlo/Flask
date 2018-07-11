# -*- coding: utf-8 -*-
# Все переменные которые создаються тут, требут импорта в main посредством from


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:111291@localhost/Flask'
    SECRET_KEY = 'Very Secret Kays'

    # SECURITY
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha256_crypt'