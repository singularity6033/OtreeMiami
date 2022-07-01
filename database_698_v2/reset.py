from pymongo import MongoClient
import pandas as pd

client = MongoClient('mongodb+srv://admin:admin@cluster0.enguk.mongodb.net/test-database?retryWrites=true&w=majority')
db = client['test-database']
csv_collection = db['csv']
record_collection = db['record']
# session_collection = db['session']
csv_list = [f'list_{str(i + 1)}.csv' for i in range(697)]

csv_collection.delete_many({})
record_collection.delete_many({})
# session_collection.delete_many({})

for csv_name in csv_list:
    print(csv_name)
    df = pd.read_csv(f'{csv_name}', header=None)
    urls = df.iloc[:, 0].tolist()
    csv_file = {
        "name": csv_name,
        "urls": urls
    }
    csv_collection.insert_one(csv_file)

record_collection = db['record']
for csv_name in csv_list:
    record = {
        "name": csv_name,
        "count": 0,
        # "session_code": -1
    }
    record_collection.insert_one(record)

# # update record
# record_collection = db['record']
# for csv_name in csv_list:
#     query = {"name": csv_name}
#     new_value = {"$set": {
#         "count": 0,
#         "session_code": -1
#     }}
#     record_collection.update_one(query, new_value)

print("Finish reset.")
