import time
from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plt

import requests

import config.azure_config as azure_config
import config.python_code as image_analysis

az = azure_config.AzureServices()

computervision_client = az.computer_vision
pictures = az.get_all_pictures()


def description_insert_image(picture):
    url = picture.get('url')
    name = picture.get('name')

    print("url", url)
    print("name", name)
    features = ['Description', 'Tags']
    img = Image.open(BytesIO(requests.get(url).content))
    fig = plt.figure(figsize=(8, 8))
    plt.title(name)
    plt.axis('off')
    plt.imshow(img)
    plt.show()

    # description_image = computervision_client.analyze_image_in_stream(img) analyzeImageInStream
    description_image = computervision_client.describe_image(url)

    description_text = ""
    for caption in description_image.captions:
        description_text = description_text + caption.text

    print("description : ", description_text, end="\n")
    # Call function to insert in BDD
    sql_picture = az.insert_pictures(name, description_text, url)
    print(sql_picture[0])
    # for tag in description_image.tags:
    #     print(tag, end="\n")

    #    az.insert_tags(tag, tag, sql_picture.id)
    # print("ok")


description_insert_image(pictures[8])

# for i in pictures:
#    description_insert_image(i)
#    time.sleep(5)
