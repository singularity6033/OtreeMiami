from pymongo import MongoClient

client = MongoClient('mongodb+srv://admin:admin@cluster0.enguk.mongodb.net/test-database?retryWrites=true&w=majority')
db = client['test-database']
csv_collection = db['csv']
record_collection = db['record']
session_collection = db['session']
csv_list = [f'list_{str(i + 1)}.csv' for i in range(697)]
#
cou = 0
for csv_name in csv_list:
    query = {"name": csv_name}
    record = record_collection.find_one(query)
    # cou += record['count']
    # if record['session_code'] == -1:
    #     cou += 1
    print(record)
# print(cou)
# query = {"name": 'n8d3mc3n'}
# print(session_collection.find_one(query))
# for x in record_collection.find({"session_code": 'p8chevey'}):
#     print(x['count'])
# print(record)
#
# print(session_collection.find_one({'name': 'tfi4zs62'}))
