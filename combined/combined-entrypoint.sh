#!/bin/bash
sh -c 'irtt client -i 10ms -d 100s -l 172 --fill=rand --sfill=rand -o /tmp/results/irtt_data.json 10.99.99.3 & python3 /tmp/ntw-meas.py & wait'
