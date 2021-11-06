import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Set environment variables
os.environ.get('SECRET_KEY') = ''
os.environ.get('SQL_SERVER') = 'virtualzoo.database.windows.net'
os.environ.get('SQL_DATABASE') = 'virtualzoo'
os.environ.get('SQL_USER_NAME') = 'useradmin'
os.environ.get('SQL_PASSWORD') = 'adminadmin123!'
os.environ.get('BLOB_ACCOUNT') = 'virtualzoo'
os.environ.get('BLOB_STORAGE_KEY') = 'GcsmRueXoxsODcceqx/4M+jzOyE+opoLVpPcA0z1uVPJJCNRzlBzc6d0JjcKi5h0FHcE7l4Vzw2uFwZkQmzQcg=='
os.environ.get('BLOB_CONTAINER') = 'images'

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or '[SQL_SERVER_GOES_HERE]'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or '[SQL_DATABASE_GOES_HERE]'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or '[SQL_USER_NAME_GOES_HERE]'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '[SQL_PASSWORD_GOES_HERE]'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or '[BLOB_ACCOUNT_GOES_HERE]'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '[BLOB_STORAGE_KEY_GOES_HERE]'
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or '[BLOB_CONTAINER_GOES_HERE]'
