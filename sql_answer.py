import sql_database

answer = "SELECT Answers FROM answer"

mycursor = sql_database.mydb.cursor()

mycursor.execute(answer)

for correct in mycursor:
    print(correct)
