import pandas as pandas
import json

data_frame = pandas.read_csv('data.tsv', sep='\t')
with open('data.json', 'w') as f:
    json.dump(data_frame.to_json(), f)