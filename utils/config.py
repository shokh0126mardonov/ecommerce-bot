import os

from dotenv import load_dotenv

load_dotenv()

class Data:
    DB_NAME = os.getenv('DB_NAME')
    DB_PASS = os.getenv('DB_PASS')
    DB_PORT = os.getenv('DB_PORT')
    DB_HOST = os.getenv('DB_HOST')
    DB_USER = os.getenv('DB_USER')
    TOKEN   = os.getenv('TOKEN')


settings = Data()

class Register:
   full_name,age,contact,confirm = range(4)
    