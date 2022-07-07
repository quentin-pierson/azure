import time
from io import BytesIO
from PIL import Image


import requests

import config.azure_config as azure_config
import config.python_code as image_analysis

az = azure_config.AzureServices()
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

print("je print mon endpoint : ",az.computer_vision_endpoint)


computervision_client = ComputerVisionClient(az.computer_vision_endpoint, CognitiveServicesCredentials(az.computer_vision_key))
pictures = az.get_all_pictures()


def description_insert_image(picture):
    print(picture)
    url = picture.get('url')
    name = picture.get('name')
    print(name)
    print("")
    img = Image.open(BytesIO(requests.get(url).content))
    description_image = computervision_client.describe_image_in_stream(img)

    # Call function to insert in BDD
    sql_picture = az.insert_pictures(name, description_image, url)
    print(sql_picture.id)

    print("ok")

description_insert_image(pictures[16])


#for i in pictures:
#    description_insert_image(i)
#    time.sleep(5)
