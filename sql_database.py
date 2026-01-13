import mysql.connector
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

mydb = mysql.connector.connect(
    host="localhost",
    user="triviabot",
    password=os.environ['SQL_PASS'],
    database="trivia_bot"
)