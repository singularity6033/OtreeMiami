from pymongo import MongoClient


client = MongoClient('mongodb+srv://admin:admin@cluster0.enguk.mongodb.net/test-database?retryWrites=true&w=majority')
db = client['test-database']
csv_collection = db['csv']
record_collection = db['record']
csv_list = [f'list_{str(i + 1)}.csv' for i in range(697)]

f = open('backup.csv', mode='w')
for cl in csv_list:
    print(cl)
    query = {'name': cl}
    record = record_collection.find_one(query)
    f.write(cl + ': ' + str(record['count']))
    f.write('\n')

print('Finished.')

