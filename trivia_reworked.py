import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
import slack.errors
from slackeventsapi import SlackEventAdapter
from datetime import datetime, timedelta
import sql_database
from ids import id_storage

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# app = Flask(__name__)
# slack_event_adapter = SlackEventAdapter(
#     os.environ['SIGNING_SECRET'],'/slack/events', app)

# client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
# BOT_ID = client.api_call("auth.test")['user_id']

#everything above supplies the crucial info to slack and the server

class Question_and_Answer:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

current_trivia = Question_and_Answer("hello", "goodbye")
for id in id_storage():
    print(current_trivia.question)
    print(current_trivia.answer)

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