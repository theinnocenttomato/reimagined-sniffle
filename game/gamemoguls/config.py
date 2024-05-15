import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    Mail_SERVER = 'smtp.googlemail.com'
    Mail_PORT = 587
    Mail_USE_TLS = True
    Mail_USERNAME = os.environ.get('EMAIL_USER')
    Mail_PASSWORD = os.environ.get('EMAIL_PASS')