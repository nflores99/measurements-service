import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import json
from pathlib import Path
import sys

X = float(sys.argv[1]) # take first imput as X
Y = float(sys.argv[2]) # take second imput as Y
num = str(sys.argv[3]) # take the input as number of dataset

# Open delay measurements
p = Path(__file__).parent.resolve()
print(p)
f1 = open(str(p)+'/irtt_data'+num+'.json') # Opening JSON file
data1 = json.load(f1) # returns JSON object as a dictionary
f1.close() # Closing file

# Open network conditions measurements
f2 = open(str(p)+'/ntw_meas_data'+num+'.json') # Opening JSON file
data2 = json.load(f2) # returns JSON object as a dictionary
f2.close() # Closing file

round_trips = data1["round_trips"]

# Lists of delays
data_rtt_list = [round_trip['delay']['rtt'] for round_trip in round_trips] # list of rtt values
data_rx_list = [round_trip['delay']['receive'] for round_trip in round_trips] # list of rx times
data_tx_list = [round_trip['delay']['send'] for round_trip in round_trips] # list of tx times
data_timestamps_list = [round_trip['timestamps']['client']['send']['wall'] for round_trip in round_trips] # list of timestamps

L = len(round_trips)
X_list = [X] * L # create a list with X value and same elements as round_trips
Y_list = [Y] * L # create a list with Y value and same elements as round_trips

# Lists of network conditions
data_ntw_cond_timestamps = [measurement['timestamp'] for measurement in data2]
data_RSRP = [measurement['RSRP'] for measurement in data2]
data_RSRQ = [measurement['RSRQ'] for measurement in data2]
data_channel = [measurement['Channel'] for measurement in data2]
data_band = [measurement['Band'] for measurement in data2]

ntw_cond_t = np.array(data_ntw_cond_timestamps)
idx = np.array([np.argmin(abs(timestamp-ntw_cond_t)) for timestamp in data_timestamps_list])

data_df = pd.DataFrame({'rtt':data_rtt_list, 
                        'send':data_tx_list, 
                        'receive':data_rx_list, 
                        'timestamp':data_timestamps_list, 
                        'X':X_list, 
                        'Y':Y_list,
                        'RSRP':[data_RSRP[i] for i in idx],
                        'RSRQ':[data_RSRQ[i] for i in idx],
                        'channel':[data_channel[i] for i in idx],
                        'band':[data_band[i] for i in idx]})

print(data_df.head(10))

table_data_rtt = pa.Table.from_pandas(data_df) # create table
pq.write_table(table_data_rtt, 'dataset_val2_'+num+'.parquet') # create parquet file 



