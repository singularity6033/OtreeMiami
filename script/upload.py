from pymongo import MongoClient
import pandas as pd

client = MongoClient('mongodb+srv://admin:admin@cluster0.enguk.mongodb.net/test-database?retryWrites=true&w=majority')
db = client['test-database']
# print(db.list_collection_names())
csv_collection = db['csv']
record_collection = db['record']
csv_list = [f'list_{str(i + 1)}.csv' for i in range(371)]

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
        "count": 0
    }
    record_collection.insert_one(record)

# update record
record_collection = db['record']
for csv_name in csv_list:
    query = {"name": csv_name}
    new_value = {"$set": {"count": 0}}
    record_collection.update_one(query, new_value)

# query = {"name": 'list_1.csv'}
# record_collection = db['record']
# record = record_collection.find_one(query)
# print(record)

print("Finish updated.")
