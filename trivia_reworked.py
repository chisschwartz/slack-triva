import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
import slack.errors
from slackeventsapi import SlackEventAdapter
import datetime
import sql_database
from ids import id_storage
import time

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

counter = 2

# day = 1

tommorow = datetime.date.today() + datetime.timedelta(days=1)
question_schedule = datetime.time(hour = 8, minute = 30)
answer_schedule = datetime.time(hour = 11, minute = 30)
schedule_question = int(datetime.datetime.combine(tommorow, question_schedule).timestamp())
schedule_answer = int(datetime.datetime.combine(tommorow, answer_schedule).timestamp())


# app = Flask(__name__)
# slack_event_adapter = SlackEventAdapter(
#     os.environ['SIGNING_SECRET'],'/slack/events', app)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']

#everything above supplies the crucial info to slack and the server

class Question_and_Answer:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

current_trivia = Question_and_Answer("hello", "goodbye")
# for id in id_storage():
#     print(current_trivia.question)
#     print(current_trivia.answer)
    # client.chat_postMessage(channel='trivia', text='Question: {}'.format(current_trivia.question))

def switch(counter):
    if counter % 2 == 0:
        current_prompt = current_trivia.question
    else:
        current_prompt = current_trivia.answer
        
    return current_prompt

# print (switch(counter))

for id in id_storage():
    try:
        response = client.chat_scheduleMessage(
            channel='trivia',
            text='Question: {}'.format(switch(counter)),
            post_at=schedule_question
    )
        print ('message success!!: ', response)
        counter += 1

    except slack.errors.SlackApiError as error:
        print('message error: ', error)

    try:
        response = client.chat_scheduleMessage(
            channel='trivia',
            text='Answer: {}'.format(switch(counter)),
            post_at=schedule_answer
    )
        print ('message success!!: ', response)
        counter += 1

    except slack.errors.SlackApiError as error:
        print('message error: ', error)
    
    # time.sleep(360)

# if __name__ == "__main__":
#     app.run(debug=True)