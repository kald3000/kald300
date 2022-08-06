import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "8934899"))
API_HASH = getenv("API_HASH", "bf3e98d2c351e4ad06946b4897374a1e")
BOT_TOKEN = getenv("BOT_TOKEN", "5184221056:AAGJrlnj4QrWnN5k44Tpwpuj-rF0qOAx1UU")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "BQAYTu6dTptmb8db-lWAW-YbG9gcaQWtuG1DlQEeSxm99aBl9be_WhgvNfXj_noXKycPFxwUNrozLON2GQvjOABF4uSllR-oggXDRpqH-l1zWKWtmGNT6MR1vZgLG_hDkrjgdJRyhie7IdA7oVx9CIqc6XjRlvI1RPyAU3DSSQw8JOU8zuxAlrPUqn3WVCBDsu-VZm18IPdit7nyZ69n69nEw1px7ETmbD9GTpBX3-OdF_Mqem_G1nkBTfGF5rrcRft4Q-AVYIjzkVO0NVeJ7JLiay9XZqFUIO1AY0Z3ytwhADD-u8rQeE6ntiu3bPc1EZQt4-6KMeKSuPM3eXJNhdCyAAAAAS2neqoA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
