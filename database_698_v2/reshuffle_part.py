import os
import random

import pandas as pd
from pymongo import MongoClient


client = MongoClient('mongodb+srv://admin:admin@cluster0.enguk.mongodb.net/test-database?retryWrites=true&w=majority')
db = client['test-database']
csv_collection = db['csv']
record_collection = db['record']
csv_list = [f'list_{str(i + 1)}.csv' for i in range(697)]

used_csv_list = []
for csv_name in csv_list:
    query = {"name": csv_name}
    record = record_collection.find_one(query)
    if record['count'] > 0:
        used_csv_list.append(csv_name)

# print(used_csv_list)
df = pd.read_csv('invalid_urls_v1.csv', header=None)
invalid_urls = df.iloc[:, 0].tolist()

csv_list = [f'list_{str(i + 1)}.csv' for i in range(698)]
part_urls = list()

for csv_name in csv_list:
    if csv_name not in used_csv_list:
        df = pd.read_csv(f'{csv_name}', header=None)
        urls = df.iloc[:, 0].tolist()
        part_urls += urls
        os.remove(csv_name)

valid_urls = list()
for url in part_urls:
    if url not in invalid_urls:
        valid_urls.append(url)

random.shuffle(valid_urls)

csv_num = len(valid_urls) // 50

new_csv_list = [f'list_{str(i + 1)}.csv' for i in range(697)]
for i in range(697):
    if new_csv_list[i] in used_csv_list:
        continue
    if len(valid_urls) < 50:
        break
    tmp = []
    for _ in range(50):
        tmp.append(valid_urls.pop())
    new_df = pd.DataFrame(tmp)
    new_df.to_csv(new_csv_list[i], index=False, header=False)

deprecated_list = '../database/list_698.csv'
new_df = pd.DataFrame(valid_urls)
new_df.to_csv(deprecated_list, index=False, header=False)

print('Finished.')

