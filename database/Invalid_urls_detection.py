import urllib.request
import pandas as pd
from tqdm import tqdm

csv_list = [f'list_{str(i + 1)}.csv' for i in range(697)]
total_urls = list()

for csv_name in csv_list:
    df = pd.read_csv(f'{csv_name}', header=None)
    urls = df.iloc[:, 0].tolist()
    total_urls += urls

invalid_urls = []
for i in tqdm(range(len(total_urls))):
    tmp = 'https://images.weserv.nl/?url=' + total_urls[i]
    try:
        status = urllib.request.urlopen(tmp).getcode()
    except:
        print('invalid url found!')
        invalid_urls.append(total_urls[i])

print('there are {} invalid urls of total 34k.'.format(len(invalid_urls)))
invalid_url_list = '../database/invalid_urls.csv'
new_df = pd.DataFrame(invalid_urls)
new_df.to_csv(invalid_url_list, index=False, header=False)
