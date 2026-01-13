import sql_database
from sql_query import storage_id

answer = "SELECT Aid, Answers FROM answer"

mycursor = sql_database.mydb.cursor()

mycursor.execute(answer)

for correct in mycursor:
    if storage_id[0] == correct[0]:
        print(correct)

# for id in storage_id:
#     if id[0] == correct[0]:
#         print("Match found for Qid {}: Answer is {}".format(id[0], correct[0]))
#     else:
#         print("No match for Qid {}".format(id[0]))

# print(storage_id)