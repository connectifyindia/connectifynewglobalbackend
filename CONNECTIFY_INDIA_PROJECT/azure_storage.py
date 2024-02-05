import os
from os.path import join, dirname
from dotenv import load_dotenv
from storages.backends.azure_storage import AzureStorage
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

print(os.environ)
# print(os.getenv('AZURE_ACCOUNT_NAME'))
# print(os.getenv('AZURE_ACCOUNT_KEY')

class AzureMediaStorage(AzureStorage):
    account_name = os.getenv('AZURE_ACCOUNT_NAME')
    account_key = os.getenv('AZURE_ACCOUNT_KEY')
    azure_container = 'media'
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    account_name = os.getenv('AZURE_ACCOUNT_NAME')
    account_key = os.getenv('AZURE_ACCOUNT_KEY')
    azure_container = 'static'
    expiration_secs = None