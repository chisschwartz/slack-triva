import sql_database

def id_storage():
    storage_id = []
             
    question_answer = "SELECT Qid FROM trivia"
    mycursor = sql_database.mydb.cursor()

    mycursor.execute(question_answer)
    for query in mycursor:
        storage_id.append(query[0])

    mycursor.close

    return storage_id