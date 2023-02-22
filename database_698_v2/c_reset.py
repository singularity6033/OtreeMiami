from pymongo import MongoClient
import pandas as pd
from tqdm import tqdm

client = MongoClient('mongodb+srv://miami:miami6033626@cluster0.lodffed.mongodb.net/?retryWrites=true&w=majority')
db = client['miami-database']
csv_collection = db['csv']
# # record_collection = db['record']
csv_names = [f'list_{str(i + 1)}.csv' for i in range(697)]
#
# csv_collection.delete_many({})
# # record_collection.delete_many({})
#
csv_list = [None] * len(csv_names)
# record_list = [None] * len(csv_names)
print('[INFO] creating collection...')
for i, csv_name in tqdm(enumerate(csv_names)):
    df = pd.read_csv(f'{csv_name}', header=None)
    urls = df.iloc[:, 0].tolist()
    csv_list[i] = {
        "name": csv_name,
        "urls": urls
    }
#     # record_list[i] = {
#     #     "name": csv_name,
#     #     "count": 0,
#     #     "prolific_ids": []
#     # }
csv_collection.insert_many(csv_list)
# record_collection.insert_many(record_list)

print("Finish reset.")
