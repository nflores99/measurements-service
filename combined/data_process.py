import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import json
from pathlib import Path
import sys

X = int(sys.argv[1]) # take first imput as X
Y = int(sys.argv[2]) # take second imput as Y

p = Path(__file__).parent.resolve()
print(p)
f = open(str(p)+'/irtt_data.json') # Opening JSON file
data = json.load(f) # returns JSON object as a dictionary
f.close() # Closing file

round_trips = data["round_trips"]

data_rtt_list = [round_trip['delay']['rtt'] for round_trip in round_trips] # list of rtt values
data_rx_list = [round_trip['delay']['receive'] for round_trip in round_trips] # list of rx times
data_tx_list = [round_trip['delay']['send'] for round_trip in round_trips] # list of tx times
data_timestamps_list = [round_trip['timestamps']['client']['send']['wall'] for round_trip in round_trips] # list of timestamps

L = len(round_trips)
X_list = [X] * L # create a list with X value and same elements as round_trips
Y_list = [Y] * L # create a list with Y value and same elements as round_trips

data_df = pd.DataFrame({'rtt':data_rtt_list, 
                        'send':data_tx_list, 
                        'receive':data_rx_list, 
                        'timestamp':data_timestamps_list, 
                        'X':X_list, 
                        'Y':Y_list})

print(data_df.head())

table_data_rtt = pa.Table.from_pandas(data_df) # create table
pq.write_table(table_data_rtt, 'irtt_data.parquet') # create parquet file 



