from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "90b8bad42e6210d0e1e04a858e045f55")
      API_ID = int(getenv("API_ID", "27680167"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "mongodb+srv://abohariyaharman2:lRekbm3GDSk0rL3v@cluster0.xfu5dov.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002670957174:-1002588279501").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
