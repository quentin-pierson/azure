import os
from azure.identity import DefaultAzureCredential
import config.config_file as config_file
import config.key_vault as key_vault

class ADLServices:
    def __init__(self, credential=None, akv_service=None):
        if credential == None:
            credential = DefaultAzureCredential()
        if akv_service == None:
            akv_service = key_vault.AKVServices(credential=credential)
