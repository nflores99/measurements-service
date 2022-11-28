
import subprocess
import json
import time

duration = 100 # seconds
sleep_time = 0.5 # seconds

meas_duration = 0
meas_list = []
t0 = time.time()
while meas_duration < duration:
    t = time.time_ns()
    res = subprocess.check_output(["curl","-s", "http://10.42.3.1:50000"])
    res = res.decode('utf-8').strip()
    res = json.loads(res)
    res['timestamp'] = t
    meas_list.append(res)
    time.sleep(sleep_time)
    meas_duration = time.time()-t0

print(meas_duration)

for elem in meas_list:
    elem['RSRP'] = elem.pop('Signal Strength')
    elem['RSRQ'] = elem.pop('Signal Quality')
    new_RSRP = float(elem['RSRP'].split()[0])
    elem['RSRP'] = new_RSRP
    new_RSRQ = float(elem['RSRQ'].split()[0])
    elem['RSRQ'] = new_RSRQ

with open("/tmp/results/ntw_meas_data.json", "w") as outfile:
    json.dump(meas_list, outfile)



    

