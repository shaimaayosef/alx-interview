#!/usr/bin/python3
"""
Log parsing
"""
import sys
import re

def print_stats(stats, filesize):
    print("File size: {}".format(filesize))
    for k in sorted(stats.keys()):
        print("{}: {}".format(k, stats[k]))

try:
    count = 0
    filesize = 0
    stats = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    pattern = re.compile(r'\S+ - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)')
    
    for line in sys.stdin:
        if pattern.match(line):
            count += 1
            data = pattern.findall(line)[0]
            status_code = data[1]
            if status_code in stats:
                stats[status_code] += 1
            filesize += int(data[2])
            if count % 10 == 0:
                print_stats(stats, filesize)
    print_stats(stats, filesize)
except KeyboardInterrupt:
    print_stats(stats, filesize)
    raise