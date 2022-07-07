import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
import config.config_file as config_file

class AKVServices:
    def __init__(self, credential=None):
        KVUri = f"https://{config_file.AKV_SERVICE}.vault.azure.net"
        if credential == None:
            credential = DefaultAzureCredential()
        self.AKV_CONFIG = SecretClient(vault_url=KVUri, credential=credential)

    def get_secret(self, name):
        return self.AKV_CONFIG.get_secret(name).value