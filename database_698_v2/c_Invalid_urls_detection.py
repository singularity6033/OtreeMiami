import time
import urllib.request
import requests
import pandas as pd
from pymongo import MongoClient
import os
from tqdm import tqdm

client = MongoClient('mongodb+srv://miami:miami6033626@cluster0.lodffed.mongodb.net/?retryWrites=true&w=majority')
db = client['miami-database']
csv_collection = db['csv']
csv_list = [f'list_{str(i + 1)}.csv' for i in range(697)]

save_path = './miami_pics/'
if not os.path.exists(save_path):
    os.makedirs(save_path)

total_urls = list()
csv = csv_collection.find({}, {'_id': 0})
for one_csv in csv:
    total_urls += one_csv['urls']


def download_image(image_url, address, fix):
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36'
    }
    r = requests.get(image_url, headers=headers)
    f = open(address + os.path.basename(fix), 'wb')
    f.write(r.content)
    f.close()
    return


print('start')

invalid_urls = []
for i in tqdm(range(len(total_urls))):
    tmp = 'https://images.weserv.nl/?url=' + total_urls[i]
    try:
        urllib.request.urlretrieve(tmp, save_path + os.path.basename(total_urls[i]))
        # status = urllib.request.urlopen(tmp).getcode()
    except:
        print('invalid url found!')
        invalid_urls.append(total_urls[i])

timestamp = time.strftime("%Y%m%d", time.localtime())
print('there are {} invalid urls of total 34k.'.format(len(invalid_urls)))
invalid_url_list = '../invalid_urls/' + str(timestamp) + '.csv'
new_df = pd.DataFrame(invalid_urls)
new_df.to_csv(invalid_url_list, index=False, header=False)
