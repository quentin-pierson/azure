import config.azure_config as azure_config

az = azure_config.AzureServices()
tags = ("suit", "watch", "man")
print(az.find_picture(tags))