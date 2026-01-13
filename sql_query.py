import sql_database

question = "SELECT Qid, Questions, Aid FROM trivia"
qid = "SELECT Aid FROM trivia"
storage_id = [1]
# dummy = [(1, 1), (2, 2)]

print(storage_id)

mycursor = sql_database.mydb.cursor()

mycursor.execute(question)

# Have the id from trivia be stored, and then send the corresponding answer
# could be stored in a variable and have logic check that all ids match up

for query in mycursor:
    print(query)

# mycursor.execute(qid)

# for id in mycursor:
#     storage_id.append(id)

print(storage_id)