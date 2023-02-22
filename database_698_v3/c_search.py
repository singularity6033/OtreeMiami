import os
import random
import pandas as pd
from pymongo import MongoClient
import numpy as np
from tqdm import tqdm

# data_path = "E:/Academia/NTU/SEC_NTU_FSR/oTree_Miami/oTree_Miami_Data"
client = MongoClient('mongodb+srv://admin:admin@cluster0.enguk.mongodb.net/test-database?retryWrites=true&w=majority')
# db = client['test-database']
# csv_collection = db['csv']
# record_collection = db['record']
# csv_list = [f'list_{str(i + 1)}.csv' for i in range(697)]

# query0 = record_collection.count_documents({"count": {'$eq': 0}})
# query1 = record_collection.count_documents({"count": {'$eq': 1}})
# query2 = record_collection.count_documents({"count": {'$eq': 2}})
# query3 = record_collection.count_documents({"count": {'$eq': 3}})
# query4 = record_collection.count_documents({"count": {'$eq': 4}})
#
# record_query = {"count": {"$eq": 1}}
# records = record_collection.find({})
# unfinished_csv_names = []
# for record in records:
#     if record['count'] <= 2:
#         unfinished_csv_names.append((record['name'], record['count']))
# query = {'name': 'list_1.csv'}
# new_records = {'$set': {
#         'count': 2,
#     }}
# record_collection.update_one(query, new_records)
# for name, count in tqdm(unfinished_csv_names):
#     query = {'name': name}
#     new_record = {'$set': {
#         'count': -1,
#     }}
#     record_collection.update_one(query, new_record)
# print(unfinished_csv_names)
# print('available spots left: ', 3 * query0 + 2 * query1 + 1 * query2)
