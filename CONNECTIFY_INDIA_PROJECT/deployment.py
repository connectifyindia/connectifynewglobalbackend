
import os
# from .settings import *
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.environ['MY_SECRET_KEY']  
# SECRET_KEY=os.environ.get('CUSTOMCONNSTR_MY_SECRET_KEY')
# print(SECRET_KEY,"secret")
# ALLOWED_HOSTS = [os.environ['Connectifyglobalbackend']]
ALLOWED_HOSTS = [os.environ.get('WEBSITE_HOSTNAME')]
# print(ALLOWED_HOSTS,'allowed_host')
# ALLOWED_HOSTS = [os.environ.get('CUSTOMCONNSTR_WEBSITE_HOSTNAME')]
CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ.get('WEBSITE_HOSTNAME')]
print(CSRF_TRUSTED_ORIGINS)


# new
SECURE_SSL_REDIRECT=1 

DEBUG = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
   ]

CORS_ALLOWED_ORIGINS = [
    'https://connectifyglobalfrontend.azurewebsites.net' 
]

STORAGES = {
    # ...
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# new
# Azure Storage Settings
DEFAULT_FILE_STORAGE = 'CONNECTIFY_INDIA_PROJECT.azure_storage.AzureMediaStorage'
# print(DEFAULT_FILE_STORAGE,'storage')
STATICFILES_STORAGE = 'CONNECTIFY_INDIA_PROJECT.azure_storage.AzureStaticStorage'
# print(STATICFILES_STORAGE,'static')

AZURE_ACCOUNT_NAME = os.getenv('AZURE_ACCOUNT_NAME')
# print(AZURE_ACCOUNT_NAME,'azure account name')
AZURE_ACCOUNT_KEY = os.getenv('AZURE_ACCOUNT_KEY')
# print(AZURE_ACCOUNT_KEY,'azure account key')

AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'

STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'


# in your setting file, eg. settings.py
host = os.getenv('AZURE_MYSQL_HOST')
# print(host,"host")
user = os.getenv('AZURE_MYSQL_USER')
# print(user,'user')
password = os.getenv('AZURE_MYSQL_PASSWORD')
# print(password,'password')
database = os.getenv('AZURE_MYSQL_NAME')
# print(database,'Database')

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME':database,
        'USER':user,
        'PASSWORD':password,
        'PORT':'3306',
        'HOST':host,
        # 'OPTIONS': {
        #     'ssl': {'ssl-ca': '/app/work/ca.pem'},
        # },
}
}


