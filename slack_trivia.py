import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
import slack.errors
from slackeventsapi import SlackEventAdapter
from datetime import datetime, timedelta
from sql_query import question
# import sql_answer as myanswer
# from sql_query import question_time

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# app = Flask(__name__)
# slack_event_adapter = SlackEventAdapter(
#     os.environ['SIGNING_SECRET'],'/slack/events', app)

# client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
# BOT_ID = client.api_call("auth.test")['user_id']


#for loop starts here

question

# myquestion
# myanswer
# print(myquestion.question_filter)
# print(myanswer.answer_filtered)

# try:
#     response = client.chat_scheduleMessage(
#         channel='',
#         text='Question: {}'.format(myquestion.question_filter),
#         post_at=int((datetime.now() + timedelta(seconds=5)).timestamp())
#     )
#     print ('message success!!: ', response)

# except slack.errors.SlackApiError as error:
#     print('message error: ', error)

#end loop here?

# if __name__ == "__main__":
#     app.run(debug=True)

#schedule messages once a day, either give four choices/true false
#respond 8-16 hours later with correct response/maybe dm user if they got correct or not
#respond with correct answer after a time period always

#MVP: bot posts once a day from a database, not repeating itself, 
#then gives an answer some hours later. Aim for 10 questions for decent sample size

#if time/energy allows make bot multiple choice. 
#Bind choices to question, or have only correct bound with 3 random choices?

#pick a random triva question to import to scheduling
#keep log of last 1-5 questions to avoid repeats
#maybe loop through all questions once, then restart with full question list
