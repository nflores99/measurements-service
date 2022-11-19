import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import json

f = open('irtt_data.json') # Opening JSON file
data = json.load(f) # returns JSON object as a dictionary
f.close() # Closing file

all = pd.DataFrame(data.items()) # create dummy dataframe
round_trips = all[1].loc[4] # pandas series

data_rtt = pd.DataFrame(columns = ['rtt']) # creation of dataframe with rtt column

for iter, val in enumerate(round_trips): # add rtt values for each packet
    a = round_trips[iter]
    data_rtt = data_rtt.append({'rtt':a['delay']['rtt']}, ignore_index=True)

print(data_rtt)

table_data_rtt = pa.Table.from_pandas(data_rtt) # create table
pq.write_table(table_data_rtt, 'data_irtt.parquet') # create parquet file
    



