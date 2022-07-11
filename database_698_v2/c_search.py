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
