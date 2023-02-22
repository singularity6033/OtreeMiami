import collections
import os
import random
import pandas as pd
from pymongo import MongoClient
from tqdm import tqdm

data_path = "../data_collected"
client = MongoClient('mongodb+srv://miami:miami6033626@cluster0.lodffed.mongodb.net/?retryWrites=true&w=majority')
db = client['miami-database']
csv_collection = db['csv']
record_collection = db['record']
csv_list = [f'list_{str(i + 1)}.csv' for i in range(697)]

dic_urls = collections.defaultdict(int)
records = record_collection.find({})

for record in tqdm(records):
    q = record['name']
    us = csv_collection.find_one({'name': q})['urls']
    for usi in us:
        dic_urls[usi] += record['count']

incomplete_urls = []
incomplete_rating = []
count = [0] * 31
for k, v in dic_urls.items():
    count[v] += 1
    if v < 3:
        incomplete_urls.append(k)
        incomplete_rating.append(v)

in_urls = {'urls': incomplete_urls,
           'count': incomplete_rating}
fv = pd.DataFrame(in_urls)
fv.to_excel('in_urls_from_database_old.xlsx', index=False)
in_urls_count = {'count_summary': [i for i in range(31)],
                 'freq': count}
fv = pd.DataFrame(in_urls_count)
fv.to_excel('in_urls_from_database_old_count.xlsx', index=False)

data_path = "E:/Academia/NTU/SEC_NTU_FSR/oTree_Miami/oTree_Miami_Data"
filenames = ['oTree_Miami_2022-05-25.xlsx', 'oTree_Miami_2022-05-28.xlsx', 'oTree_Miami_2022-06-04.xlsx',
             'oTree_Miami_2022-06-14.xlsx', 'oTree_Miami_2022-06-17.xlsx', 'oTree_Miami_2022-06-21.xlsx',
             'oTree_Miami_2022-06-28.xlsx', 'oTree_Miami_2022-07-06.xlsx', 'oTree_Miami_2022-07-23.xlsx',
             'oTree_Miami_2022-07-27.xlsx', 'oTree_Miami_2022-07-28.xlsx', 'oTree_Miami_2022-07-30.xlsx',
             'oTree_Miami_2022-08-02.xlsx', 'oTree_Miami_2022-08-05.xlsx', 'oTree_Miami_2022-08-10.xlsx',
             'oTree_Miami_2022-08-16.xlsx', 'oTree_Miami_2022-08-18.xlsx', 'oTree_Miami_2022-08-19.xlsx',
             'oTree_Miami_2022-08-20.xlsx', 'oTree_Miami_2022-08-23.xlsx']

urls_variable = ['bam122.' + str(i + 1) + '.player.normal_pic_url' for i in range(50)]
usecols = ['bam122.51.player.AC_Correctness'] + urls_variable
df = pd.read_csv('../invalid_urls/20220520.csv', header=None)
invalid_urls = df.iloc[:, 0].tolist()


def convert_excel_columns_to_list():
    u_dic = collections.defaultdict(int)
    for filename in tqdm(filenames):
        df = pd.read_excel(os.path.join(data_path, filename), usecols=usecols)
        df_li = df.values.tolist()
        for i, item in enumerate(df_li):
            if item[-1] >= 0.5:
                for j in item[:-1]:
                    u_dic[j] += 1
    return u_dic


def convert_excel_columns_to_list_exclude_invalid():
    u_dic = collections.defaultdict(int)
    for filename in tqdm(filenames):
        df = pd.read_excel(os.path.join(data_path, filename), usecols=usecols)
        df_li = df.values.tolist()
        for i, item in enumerate(df_li):
            if item[-1] >= 0.5:
                for j in item[:-1]:
                    if j not in invalid_urls:
                        u_dic[j] += 1
    return u_dic


dic = convert_excel_columns_to_list()
dic_in = convert_excel_columns_to_list_exclude_invalid()
incomplete_urls1 = []
incomplete_rating1 = []
incomplete_urls2 = []
incomplete_rating2 = []
count1 = [0] * 31
count2 = [0] * 31
for k, v in dic.items():
    count1[v] += 1
    if v < 3:
        incomplete_urls1.append(k)
        incomplete_rating1.append(v)
for k, v in dic_in.items():
    count2[v] += 1
    if v < 3:
        incomplete_urls2.append(k)
        incomplete_rating2.append(v)

in_urls1 = {'urls': incomplete_urls1,
            'count': incomplete_rating1}
fv = pd.DataFrame(in_urls1)
fv.to_excel('in_urls_from_real_collections.xlsx', index=False)
in_urls1_count = {'count_summary': [i for i in range(31)],
                  'freq': count}
fv = pd.DataFrame(in_urls1_count)
fv.to_excel('in_urls_from_real_collections_count.xlsx', index=False)

in_urls2 = {'urls': incomplete_urls2,
            'count': incomplete_rating2}
fv = pd.DataFrame(in_urls2)
fv.to_excel('in_urls_from_real_collections_ex_invalid.xlsx', index=False)
in_urls2_count = {'count_summary': [i for i in range(31)],
                  'freq': count2}
fv = pd.DataFrame(in_urls2_count)
fv.to_excel('in_urls_from_real_collections_ex_invalid_count.xlsx', index=False)

total_urls = list()
for csv_name in tqdm(csv_list):
    query = {"name": csv_name}
    record = csv_collection.find_one(query)
    total_urls.append(record['urls'])

tmp = 0
for iu0 in incomplete_urls:
    if iu0 in incomplete_urls2:
        tmp += 1
print(tmp)

updated_list = []
updated_num = []
for i, r in tqdm(enumerate(incomplete_urls2)):
    for j in range(len(total_urls)):
        if r not in incomplete_urls and r in total_urls[j] and csv_list[j] not in updated_list:
            updated_num.append(incomplete_rating2[i])
            updated_list.append(csv_list[j])
print(updated_list)

dic_urls_new = collections.defaultdict(int)
records1 = record_collection.find({})
for record in tqdm(records1):
    q = record['name']
    us = csv_collection.find_one({'name': q})['urls']
    if q not in updated_list:
        for usi in us:
            dic_urls_new[usi] += record['count']
    else:
        for usi in us:
            dic_urls_new[usi] += updated_num[updated_list.index(q)]

incomplete_urls_new = []
incomplete_rating_new = []
count_new = [0] * 31
for k, v in dic_urls_new.items():
    count_new[v] += 1
    if v < 3:
        incomplete_urls_new.append(k)
        incomplete_rating_new.append(v)

in_urls_new = {'urls': incomplete_urls_new,
               'count': incomplete_rating_new}
fv = pd.DataFrame(in_urls_new)
fv.to_excel('in_urls_from_database_new.xlsx', index=False)
in_urls_new_count = {'count_summary': [i for i in range(31)],
                     'freq': count_new}
fv = pd.DataFrame(in_urls_new_count)
fv.to_excel('in_urls_from_database_new_count.xlsx', index=False)

for i, v in tqdm(enumerate(updated_list)):
    query = {'name': v}
    new_record = {'$set': {
        'count': updated_num[i]
    }}
    record_collection.update_one(query, new_record)

for i, iu0 in enumerate(incomplete_urls_new):
    if iu0 in incomplete_urls2 and incomplete_rating2[incomplete_urls2.index(iu0)] == incomplete_rating_new[i]:
        tmp += 1
print(tmp)
