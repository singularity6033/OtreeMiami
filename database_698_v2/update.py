from pymongo import MongoClient
import pandas as pd

client = MongoClient('mongodb+srv://admin:admin@cluster0.enguk.mongodb.net/test-database?retryWrites=true&w=majority')
db = client['test-database']
csv_collection = db['csv']
record_collection = db['record']

csv_list = [f'list_{str(i + 1)}.csv' for i in range(697)]

for csv_name in csv_list:
    print(csv_name)
    df = pd.read_csv(f'{csv_name}', header=None)
    urls = df.iloc[:, 0].tolist()
    query = {"name": csv_name}
    new_value = {"$set": {
        "urls": urls
    }}
    csv_collection.update_one(query, new_value)

print("Finish update.")
