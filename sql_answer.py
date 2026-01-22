import sql_database
from sql_query import storage_id
from sql_query import query_id

answer_raw = "SELECT Aid, Answers FROM answer"

mycursor = sql_database.mydb.cursor()

mycursor.execute(answer_raw)

for correct in mycursor:
    answer_filtered = correct[1]

    if correct[0] == query_id:
        print(answer_filtered)