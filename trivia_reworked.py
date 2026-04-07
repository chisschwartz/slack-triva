import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
import slack.errors
from slackeventsapi import SlackEventAdapter
from datetime import datetime, timedelta
import sql_database

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# app = Flask(__name__)
# slack_event_adapter = SlackEventAdapter(
#     os.environ['SIGNING_SECRET'],'/slack/events', app)

# client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
# BOT_ID = client.api_call("auth.test")['user_id']

#everything above supplies the crucial info to slack and the server

storage_id = []

question_answer = "SELECT Qid, Questions, Answers FROM trivia"
mycursor = sql_database.mydb.cursor()

mycursor.execute(question_answer)
for query in mycursor:
    storage_id.append(query[0])

mycursor.close


class Question_and_Answer:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

current_trivia = Question_and_Answer("hello", "goodbye")
print(current_trivia.question)
print(current_trivia.answer)
print(storage_id)

# try:
#     response = client.chat_scheduleMessage(
#         channel='',
#         text='Question: {}'.format(myquestion.question_filter),
#         post_at=int((datetime.now() + timedelta(seconds=5)).timestamp())
#     )
#     print ('message success!!: ', response)

# except slack.errors.SlackApiError as error:
#     print('message error: ', error)

# if __name__ == "__main__":
#     app.run(debug=True)