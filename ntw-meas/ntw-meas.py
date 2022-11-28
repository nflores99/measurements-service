
import subprocess
import json
import time

duration = 2 # seconds
sleep_time = 0.5 # seconds

meas_duration = 0

init = time.monotonic()
while meas_duration < duration:
    t = time.time_ns()
    res = subprocess.check_output(["curl","http://10.10.5.1:50000"])
    res = res.decode('utf-8').strip()
    res = json.loads(res)
    res['timestamp'] = t
    print(res)
    time.sleep(sleep_time)
    meas_duration += sleep_time

print(init-time.monotonic())
    

