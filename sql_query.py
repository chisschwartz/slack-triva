import sql_database
import random

question = "SELECT Qid, Questions, Aid FROM trivia"
question_answer = "SELECT Aid, Answers FROM answer"
storage_id = []
query_id = 0
random_id = ""
used_id = []

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
            query_id = query[0]
            
        if query_id in storage_id:
            if query_id == query[2]:
                print(storage_id)
                print(query_id)
                return question_filter
    
    print(question_maker())

    random_id = random.choice(storage_id)
        if random_id not in used_id:
            
    used_id.append(random_id)

    print(random_id)

    # def answer():

    #     answer_id = 0

    #     mycursor.execute(question_answer)

    #     for answer in mycursor:
    #         answer_id = answer[0]
    #         answer_filter = answer[1]

    #         if answer_id in storage_id:
    #             if answer_id == query_id:
    #                 return answer_filter
    # print(answer())