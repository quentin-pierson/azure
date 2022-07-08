import config.azure_config as azure_config

az = azure_config.AzureServices()
#tags = ("suit", "watch", "man")
tags = ["suit", "man"]

if __name__ == '__main__':
    print(az.find_picture(tags))