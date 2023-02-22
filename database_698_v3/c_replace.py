import os
import random

import pandas as pd
from pymongo import MongoClient


client = MongoClient('mongodb+srv://admin:admin@cluster0.enguk.mongodb.net/test-database?retryWrites=true&w=majority')
db = client['test-database']
csv_collection = db['csv']
record_collection = db['record']
csv_list = [f'list_{str(i + 1)}.csv' for i in range(697)]

df = pd.read_csv('../invalid_urls/20220521.csv', header=None)
invalid_urls = df.iloc[:, 0].tolist()

######
# test urls validation in dataset
urls = list()
for csv_name in csv_list:
    query = {"name": csv_name}
    record = csv_collection.find_one(query)
    urls += record['urls']

for url in urls:
    if url in invalid_urls:
        print('error')
######

######
# replace the front with the behind side
# damaged_csv_list = []
# for csv_name in csv_list:
#     df = pd.read_csv(f'{csv_name}', header=None)
#     urls = df.iloc[:, 0].tolist()
#     for url in urls:
#         if url in invalid_urls:
#             damaged_csv_list.append(csv_name)
#             break
# print(len(damaged_csv_list))
#
# for csv_name in damaged_csv_list:
#     df = pd.read_csv(f'{csv_name}', header=None)
#     urls = df.iloc[:, 0].tolist()
#     i = csv_list.index(csv_name) + 1
#     while csv_list[i] in damaged_csv_list:
#         i += 1
#     temp_valid_csv = csv_list[i]
#     df = pd.read_csv(temp_valid_csv, header=None)
#     valid_urls = df.iloc[:, 0].tolist()
#     for i in range(len(urls)):
#         if urls[i] in invalid_urls:
#             tmp = valid_urls.pop()
#             urls[i] = tmp
#     os.remove(csv_name)
#     new_df = pd.DataFrame(urls)
#     new_df.to_csv(csv_name, index=False, header=False)
######

######
# naive replacement (sequentially)
# for csv_name in csv_list:
#     query = {"name": csv_name}
#     record = record_collection.find_one(query)
#     if record['count'] == 0 and csv_name not in damaged_csv_list:
#         df = pd.read_csv(f'{csv_name}', header=None)
#         urls = df.iloc[:, 0].tolist()
#         for url in urls:
#             valid_urls.append(url)
#             if len(valid_urls) == len(invalid_urls):
#                 break
#         if len(valid_urls) == len(invalid_urls):
#             break
#
# for csv_name in damaged_csv_list:
#     df = pd.read_csv(f'{csv_name}', header=None)
#     urls = df.iloc[:, 0].tolist()
#     for i in range(len(urls)):
#         if urls[i] in invalid_urls:
#             tmp = valid_urls.pop()
#             urls[i] = tmp
#     os.remove(csv_name)
#     new_df = pd.DataFrame(urls)
#     new_df.to_csv(csv_name, index=False, header=False)
#######
print('finished')
