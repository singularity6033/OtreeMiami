import os

import pandas as pd
from tqdm import tqdm

csv_list = [f'list_{str(i + 1)}.csv' for i in range(697)]
save_path = '../database_698_v3/'
if not os.path.exists(save_path):
    os.makedirs(save_path)

for csv_name in tqdm(csv_list):
    df = pd.read_csv(f'{csv_name}', header=None)
    old_list = df.iloc[:, 0].tolist()
    new_list = []
    for old_url in old_list:
        filename = os.path.basename(old_url)
        new_url = 'https://expernomics.com/miami/' + filename
        new_list.append(new_url)
    new_df = pd.DataFrame(new_list)
    new_df.to_csv(save_path + csv_name, index=False, header=False)