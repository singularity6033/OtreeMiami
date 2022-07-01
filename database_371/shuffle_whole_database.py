import random
import pandas as pd

csv_list = [f'list_{str(i + 1)}.csv' for i in range(371)]
total_urls = list()

for csv_name in csv_list:
    df = pd.read_csv(f'{csv_name}', header=None)
    urls = df.iloc[:, 0].tolist()
    total_urls += urls

random.shuffle(total_urls)

csv_num = len(total_urls) // 50
new_csv_list = [f'../database/list_{str(i + 1)}.csv' for i in range(csv_num)]
for i in range(csv_num):
    new_df = pd.DataFrame(total_urls[50*i:50*(i+1)])
    new_df.to_csv(new_csv_list[i], index=False, header=False)

deprecated_list = '../database/list_698.csv'
new_df = pd.DataFrame(total_urls[50*csv_num:])
new_df.to_csv(deprecated_list, index=False, header=False)

print('Finished.')
