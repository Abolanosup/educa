import os
# Bot
BOT_TOKEN = '5444581119:AAFTxQF9x0RXHsMA58rXCpCrAYQIrTEDl3A'
TG_API_ID = '13233271'
TG_API_HASH = 'e3ce8145aa657c2a4cc5cf0f7183e476'
TG_ADMIN = 'Ghosthell0210'

# Database
DB_LOCAL = False
DB_HOST = 'sql.freedb.tech'
DB_HOST_USERNAME = ''
DB_HOST_PASSWORD = ''
DB_NAME = ''

if DB_LOCAL:
    # Database Local
    DB_HOST = ''
    DB_HOST_USERNAME = 'root'
    DB_HOST_PASSWORD = ''
    DB_NAME = 'clutilprodb'
