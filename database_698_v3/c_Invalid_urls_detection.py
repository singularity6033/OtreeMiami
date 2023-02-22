import time
import urllib.request
import pandas as pd
from pymongo import MongoClient
import os
from tqdm import tqdm

client = MongoClient('mongodb+srv://miami:miami6033626@cluster0.lodffed.mongodb.net/?retryWrites=true&w=majority')
db = client['miami-database']
csv_collection = db['csv']
csv_list = [f'list_{str(i + 1)}.csv' for i in range(697)]

total_urls = list()
csv = csv_collection.find({}, {'_id': 0})
for one_csv in csv:
    total_urls += one_csv['urls']

print('start')

invalid_urls = []
for i in tqdm(range(len(total_urls))):
    try:
        status = urllib.request.urlopen(total_urls[i]).getcode()
    except:
        print('invalid url found!')
        invalid_urls.append(total_urls[i])

timestamp = time.strftime("%Y%m%d", time.localtime())
print('there are {} invalid urls of total 34k.'.format(len(invalid_urls)))
invalid_url_list = '../invalid_urls/' + str(timestamp) + '.csv'
new_df = pd.DataFrame(invalid_urls)
new_df.to_csv(invalid_url_list, index=False, header=False)
