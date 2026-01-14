import sql_database

question = "SELECT Qid, Questions, Aid FROM trivia"
qid = "SELECT Aid FROM trivia"
storage_id = []

print(storage_id)

mycursor = sql_database.mydb.cursor()

mycursor.execute(question)

#for loop that to iterate over question so that only one question is given
#could be stored in the main function?

for query in mycursor:
    # print(query)
    question_filter = query[1]
    # print(question_filter)
    storage_id.append((query[0]))


# mycursor.execute(qid)

# for id in mycursor:
#     storage_id.append(id)

print(storage_id)