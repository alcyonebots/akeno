import json
import os


def get_user_list(config, key):
    with open("{}/Emilia/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    API_HASH = "22878444" # API_HASH from my.telegram.org
    API_ID = 550641aa3600a98c1cb94afc259f2244 # API_ID from my.telegram.org

    BOT_ID = 7887377098 # BOT_ID
    BOT_USERNAME = "AkenoHajimeBot" # BOT_USERNAME

    MONGO_DB_URL = "mongodb+srv://Akeno:Hajime@akeno.zyn9h.mongodb.net/" # MongoDB URL from MongoDB Atlas

    SUPPORT_CHAT = "Alcyone_Support" # Support Chat Username
    UPDATE_CHANNEL = "AlcyoneBots" # Update Channel Username
    START_PIC = "https://pic-bstarstatic.akamaized.net/ugc/9e98b6c8872450f3e8b19e0d0aca02deff02981f.jpg@1200w_630h_1e_1c_1f.webp" # Start Image
    DEV_USERS = [6663845789, 6698364560] # Dev Users
    TOKEN = "7887377098:AAGPD37rvqymDGiv3R2xXXvqL4p70GxnWB8" # Bot Token from @BotFather
    CLONE_LIMIT = 50 # Number of clones your bot can make

    EVENT_LOGS = -1002183841044 # Event Logs Chat ID
    OWNER_ID = 6663845789 # Owner ID
 
    TEMP_DOWNLOAD_DIRECTORY = "root/" # Temporary Download Directory
    BOT_NAME = "Akeno" # Bot Name
    WALL_API = "6950f53" # Wall API from wall.alphacoders.com
    ORIGINAL_EVENT_LOOP = True # Do not Change


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
