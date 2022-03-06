import pandas as pd

csv_list = [f'list_{str(i + 1)}.csv' for i in range(371)]

for csv_name in csv_list:
    print(csv_name)
    df = pd.read_csv(f'../_static/csv/{csv_name}', header=None)
    df = df.iloc[0:94]
    df.to_csv(csv_name, index=False, header=False)
