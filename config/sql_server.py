import sqlalchemy
from azure.identity import DefaultAzureCredential

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
        driver = "{ODBC Driver 18 for SQL Server}"

        self.conn = pyodbc.connect(f'DRIVER={driver};SERVER=' + sql_server + ';DATABASE=' + sql_database + ';UID='
                                   + sql_user + ';PWD=' + sql_password)

    def execute_request(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()
        return cursor

    def execute_request_without_commit(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor

    def execute_request_fetch(self, query):
        cursor = self.execute_request_without_commit(query)
        val = cursor.fetchall()
        cursor.close()
        return val

    def execute_exec_request(self, query, params):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        return cursor

    def execute_exec_request_without_commit(self, query, params):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return cursor

    def execute_exec_request_fetch(self, query, params):
        cursor = self.execute_exec_request(query, params)
        cursor2 = self.execute_exec_request_without_commit(query, params)
        val = cursor2.fetchall()
        cursor.close()
        cursor2.close()
        print(f"val : {val}")
        return val

    def get_tags(self):
        query = "EXEC SP_GET_TAGS;"
        return self.execute_request_fetch(query)

    def get_picture(self, tags):
        query = "EXEC SP_GET_PICTURES;"
        return self.execute_request_fetch(query)

    def insert_tags(self, key, value, id):
        query = f"EXEC SP_SET_TAG ?, ?, ?;"
        params = (key, value, id)
        return self.execute_exec_request(query, params)

    def insert_pictures(self, name, description, link):
        query = f"Exec SP_SET_PICTURE ?, ?, ?;"
        params = (name, description, link)
        return self.execute_exec_request_fetch(query, params)
