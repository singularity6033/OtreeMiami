import time
from tqdm import tqdm
from pymongo import MongoClient

client = MongoClient('mongodb+srv://admin:admin@cluster0.enguk.mongodb.net/test-database?retryWrites=true&w=majority')
db = client['test-database']
csv_collection = db['csv']
record_collection = db['record']
csv_list = [f'list_{str(i + 1)}.csv' for i in range(697)]
timestamp = time.strftime("%Y%m%d", time.localtime())

f = open('backup_' + str(timestamp) + '.csv', mode='a')
records = record_collection.find({}, {"_id": 0})
for record in tqdm(records):
    f.write(record['name'] + ': ' + str(record['count']) + ',' + str(record['prolific_ids']))
    f.write('\n')
print('Finished.')
