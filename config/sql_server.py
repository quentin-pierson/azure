from azure.identity import DefaultAzureCredential
import sqlalchemy as sa
from sqlalchemy import create_engine
import urllib
from urllib.parse import quote_plus

import pyodbc
import config.config_file as config_file
import config.key_vault as key_vault

class SQLService:
    def __init__(self, credential=None, akv_service=None):
        if credential == None:
            credential = DefaultAzureCredential()
        if akv_service == None:
            akv_service = key_vault.AKVServices(credential=credential)

        sql_server = akv_service.get_secret(config_file.AKV_SQL_SERVER)
        sql_port = "1433"
        sql_database = akv_service.get_secret(config_file.AKV_SQL_DATABASE)
        sql_user = akv_service.get_secret(config_file.AKV_SQL_ADMIN_USER)
        sql_password = akv_service.get_secret(config_file.AKV_SQL_ADMIN_SECRET)
        driver = "{ODBC Driver 13 for SQL Server}"
        sa_url = f"mssql+pyodbc://{sql_user}:{sql_password}@{sql_server}:{sql_port}/{sql_database}?driver={driver}??trusted_connection=yes"
        self.conn = create_engine(sa_url)

    def execute_request(self, query):
        result = self.conn.execute(query).fetchall()
        return result

    def get_tags(self):
        query = "EXEC SP_GET_TAGS;"
        return self.execute_request(query)

    def insert_tags(self):
        pass

    def insert_pictures(self):
        pass
