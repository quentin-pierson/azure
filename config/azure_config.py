import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

import config.blob as blob
import config.config_file as config_file
import config.key_vault as key_vault
import config.sql_server as sql_server

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials


class AzureServices:
    def __init__(self):
        self.credential = DefaultAzureCredential()
        self.akv_service = key_vault.AKVServices(self.credential)
        self.adl_service = blob.ADLServices(self.credential, self.akv_service)
        self.sql_service = sql_server.SQLService(self.credential, self.akv_service)
        computer_vision_key = self.akv_service.get_secret(config_file.AKV_CV_KEY)
        computer_vision_endpoint = self.akv_service.get_secret(config_file.AKV_CV_ENDPOINT)
        self.computer_vision = ComputerVisionClient(computer_vision_endpoint,
                                                    CognitiveServicesCredentials(computer_vision_key))

    def get_secret(self, name):
        return self.akv_service.get_secret(name)

    def get_tags(self):
        return self.sql_service.get_tags()

    def get_picture(self, tags):
        return self.sql_service.get_picture(tags)

    def insert_tags(self, key, value, id):
        return self.sql_service.insert_tags(key, value, id)

    def insert_pictures(self, name, description, link):
        return self.sql_service.insert_pictures(name, description, link)

    def get_all_pictures(self):
        return self.adl_service.get_all_pictures()

    def find_picture(self, tags):
        def most_frequent(List):
            return max(set(List), key=List.count)
        result = []
        for tag in tags:
            val = self.sql_service.get_picture_by_tag(tag)
            for t in val:
                result.append(t[0])

        return self.sql_service.get_picture_by_id(most_frequent(result))[3]