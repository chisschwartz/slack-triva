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

mycursor = mydb.cursor()

id = "SELECT Id FROM trivia"

question = "SELECT Questions FROM trivia"
answer = "SELECT CorrectChoice FROM answer"

mycursor.execute(question)

for x in mycursor:
    print(x)