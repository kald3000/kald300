import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "9305835"))
API_HASH = getenv("API_HASH", "a60c62f35b0db984f6fb6b9421e805d3")
BOT_TOKEN = getenv("BOT_TOKEN", "5789746319:AAEEUCuPjS3cdwm3Rp0GpQMXq0XNfQDlYBQ")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "BADCzxDXwy8ZixpjjiF7Ta5CRUczsYNl8OmmKv-FFdagx2zgcm6OjDN7PlB4mkrvWBVDtJzFFQPD2gqjsn2UFFomRI0uF7qsvoHSzk8n1KJpViER8sAxnfaPCHCR6fsRnebfhPBf-JYU8SX0EB7h-V3nGmfz57KhyXSfjCqf5ZqVOQnUxyOk8nGQtTgBv-w4XU-RmAzody7Ya7VBxDWxKkddj0kw1oVMg6Jv2VI_1zmgaunU7IaMyQMnYqzXokXa0ANNtsmu3u1i5YalSyHs3OzUo6aUbaXMVo_wZRPTSXx1h8pQN6vsocIxoMGwMrpQn2PrSqaCRsar5rEFI0rfz2EgAAAAAVdVw7kA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
