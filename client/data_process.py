import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import json
from pathlib import Path

p = Path(__file__).parent.resolve()
print(p)
f = open(str(p)+'/irtt_data.json') # Opening JSON file
data = json.load(f) # returns JSON object as a dictionary
f.close() # Closing file
"""
all = pd.DataFrame(data.items()) # create dummy dataframe
round_trips = all[1].loc[4] # pandas series
"""
round_trips = data["round_trips"]
data_rtt = pd.DataFrame(columns = ['rtt']) # creation of dataframe with rtt column

data_rtt_list = [round_trip['delay']['rtt'] for round_trip in round_trips] # list of rtt values
data_rx_list = [round_trip['delay']['receive'] for round_trip in round_trips] # list of rx times
data_tx_list = [round_trip['delay']['send'] for round_trip in round_trips] # list of tx times

data_df = pd.DataFrame({'rtt':data_rtt_list, 'receive':data_rx_list, 'send':data_tx_list})

"""
for iter, val in enumerate(round_trips): # add rtt values for each packet
    a = round_trips[iter]
    data_rtt = data_rtt.append({'rtt':a['delay']['rtt']}, ignore_index=True)
"""

print(data_df)
"""
table_data_rtt = pa.Table.from_pandas(data_df) # create table
pq.write_table(table_data_rtt, 'irtt_data.parquet') # create parquet file
"""   



