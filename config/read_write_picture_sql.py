import config.azure_config as azure_config
import config.python_code as image_analysis

az = azure_config.AzureServices()
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

print("je print mon endpoint : ",az.computer_vision_endpoint)


computervision_client = ComputerVisionClient(az.computer_vision_endpoint, CognitiveServicesCredentials(az.computer_vision_key))

#az.insert_tags("droite", "gauche")
az.get_container()
print("tages ",az.get_tags())


def description_tag_image(image_path):
    image_stream = open(image_path, "rb")
    description = computervision_client.describe_image_in_stream(image_stream)


    for tag in description.tags:
        pass

    for caption in description.captions:
        print(caption.text)