import pandas as pd
import collections
import os
from tqdm import tqdm

from pymongo import MongoClient

data_path = "E:/Academia/NTU/SEC_NTU_FSR/oTree_Miami/oTree_Miami_Data"
filenames = ['oTree_Miami_2022-05-25.xlsx', 'oTree_Miami_2022-05-28.xlsx', 'oTree_Miami_2022-06-04.xlsx',
             'oTree_Miami_2022-06-14.xlsx', 'oTree_Miami_2022-06-17.xlsx', 'oTree_Miami_2022-06-21.xlsx',
             'oTree_Miami_2022-06-28.xlsx', 'oTree_Miami_2022-07-06.xlsx']


def convert_excel_columns_to_list():
    pass_samples = collections.defaultdict(list)
    for filename in tqdm(filenames):
        df = pd.read_excel(os.path.join(data_path, filename),
                           usecols=['participant.label', 'bam122.51.player.AC_Correctness',
                                    'bam122.51.player.csv_file_used'])
        df_li = df.values.tolist()
        for label, acc, csv_n in df_li:
            if not pass_samples[csv_n]:
                pass_samples[csv_n] = [list(), 0]
            if acc >= 0.5:
                pass_samples[csv_n][0].append(label)
                pass_samples[csv_n][1] += 1
    return pass_samples


if __name__ == '__main__':
    valid_csv_used = convert_excel_columns_to_list()
    client = MongoClient(
        'mongodb+srv://admin:admin@cluster0.enguk.mongodb.net/test-database?retryWrites=true&w=majority')
    db = client['test-database']
    record_collection = db['record']

    csv_list = [f'list_{str(i + 1)}.csv' for i in range(697)]
    for k, v in tqdm(valid_csv_used.items()):
        query = {'name': k}
        new_record = {'$set': {
            'count': v[1],
            'prolific_ids': v[0]
        }}
        record_collection.update_one(query, new_record)
