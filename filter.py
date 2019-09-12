#!/usr/bin/env python3

import json
import os

# Make a list of log files in the current directory
logs = [f for f in os.listdir() if f.endswith(".log")]
logs.sort()

# For each log we find, open it and load json objects one at a time and make a
# list of them
for fname in logs:
    data = []
    with open(fname) as f:
        for line in f:
            data.append(json.loads(line))

# Find scan events for mainstars where StarType is one of our targets and make
# lists of matching stars
    scans = list(filter(lambda ev: ev['event'] == 'Scan', data))
    scans_mainstar = list(filter(lambda ev: ev['DistanceFromArrivalLS'] == 0.000000, scans))
    scans_mainstar_F = list(filter(lambda ev: ev['StarType'] == 'F', scans_mainstar))
    scans_mainstar_G = list(filter(lambda ev: ev['StarType'] == 'G', scans_mainstar))
    scans_mainstar_K = list(filter(lambda ev: ev['StarType'] == 'K', scans_mainstar))

# Iterate over each of our lists of matching stars, pop off the binary suffix if
# it exists, and print the results
    for systems in scans_mainstar_F:
        fstar = str(systems['BodyName'])
        if fstar[-2:] == ' A':
            print(fstar[:-2])
        else:
            print(fstar)
    for systems in scans_mainstar_G:
        gstar = str(systems['BodyName'])
        if gstar[-2:] == ' A':
            print(gstar[:-2])
        else:
            print(gstar)
    for systems in scans_mainstar_K:
        kstar = str(systems['BodyName'])
        if kstar[-2:] == ' A':
            print(kstar[:-2])
        else:
            print(kstar)
