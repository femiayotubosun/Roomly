"""
Flask Config.
"""
from logging import DEBUG
from os import environ, path
from dotenv import load_dotenv

# Load .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """
    Config Class
    : Set flask config variables
    """
    DEBUG = True
    SECRET_KEY = environ.get('APP_SECRET_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    UPLOAD_EXTENSIONS = ['.jpg', '.png', '.gif']
    UPLOAD_FOLDER = '/static/img/user_photos'

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # FLASK-uPLOADS
    UPLOADED_FILES_DEST = 'static'
