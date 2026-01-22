import sql_database

question = "SELECT Qid, Questions, Aid FROM trivia"
storage_id = []
query_id = 1

mycursor = sql_database.mydb.cursor()

# def add_one():
#     global query_id
#     query_id += 1

class question:

    def question_maker():

        mycursor.execute(question)
        
        global query_id

        for query in mycursor:
            storage_id.append((query[0]))
            question_filter = query[1]
    
            if query_id in storage_id:
                if query_id == query[2]:
                    print(storage_id)
                    print(query_id)
                    return question_filter
    
    print(question_maker())            