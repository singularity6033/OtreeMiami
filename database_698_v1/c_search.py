import pandas as pd
from pymongo import MongoClient

client = MongoClient('mongodb+srv://admin:admin@cluster0.enguk.mongodb.net/test-database?retryWrites=true&w=majority')
db = client['test-database']
csv_collection = db['csv']
record_collection = db['record']
csv_list = [f'list_{str(i + 1)}.csv' for i in range(697)]

query1 = record_collection.count_documents({"count": {'$eq': 1}})
query2 = record_collection.count_documents({"count": {'$eq': 2}})
query3 = record_collection.count_documents({"count": {'$eq': 3}})

print('available spots left: ', len(csv_list) * 3 - 3 * query3 - 2 * query2 - query1)

df = pd.read_csv('../invalid_urls/20220520.csv', header=None)
invalid_urls = df.iloc[:, 0].tolist()

total_urls = list()
for csv_name in csv_list:
    print(csv_name)
    query = {"name": csv_name}
    record = csv_collection.find_one(query)
    total_urls += record['urls']
c = 0
for iu in invalid_urls:
    if iu in total_urls:
        c += 1
print(c)
