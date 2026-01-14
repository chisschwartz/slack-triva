import sql_database
from sql_query import storage_id

answer_raw = "SELECT Aid, Answers FROM answer"

mycursor = sql_database.mydb.cursor()

mycursor.execute(answer_raw)

for correct in mycursor:
    if storage_id[0] == (correct[0], ):
        # print(correct)
        answer_filtered = correct[1]
        # print(answer_filtered)

storage_id.clear()