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
BOT_TOKEN = getenv("BOT_TOKEN", "5470379119:AAEDMGrx3kBLVDo4LtA_gqeyJNoYfg7p97A")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "AgBtpJe8wuTdrOHlbHIk-c_QsC1tC3uKgg5QxG7h_jsESDx0sGRKWX8KCGNtYdBYKusWdz0m9k6tO30fQpN_F_MZMAU6AAIxr6NBSU-OKKVUK-2m5xRTmI8bsCtcPl-uUW5m2GLjZxkMm3VgoZuYZXnjR9kL5nTSSnOcky1KTubSgrMt53ib01kOzVcU3HUIuk3VKoGIm9W8YXv9npeIojmGpIXVtYtlsz3-UehmxPGjvTsaKOA85IZLxJ6IjbgglMyg7XhzfGFyk02afVFfdweE90Cg3dADxI6DDE_6AJQx19hYGtTREsctvwLUSLcf4_0VbLC1K8t5jXOpZmzsQ_qoAAAAAT5qK54A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
