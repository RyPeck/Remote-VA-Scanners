#!/usr/bin/env python3

import csv
import ipaddress

scanners = []

with open("scanners.csv") as f:
    scan_reader = csv.DictReader(f)
    scanners = list(scan_reader)

# Verify that we have a list of valid IP Addresses/CIDRs
for line in scanners:
    ip_object = ipaddress.IPv4Network(line['cidr'])
    line['ip_object'] = ip_object

# Print CIDR List of IP's
for line in scanners:
    print(line['ip_object'])

# Comma separated single line list
print(','.join([str(l['ip_object']) for l in scanners]))
