import sql_database

question = "SELECT Qid, Questions FROM trivia"

mycursor = sql_database.mydb.cursor()

mycursor.execute(question)

# Have the id from trivia be stored, and then send the corresponding answer

for query in mycursor:
    print(query)