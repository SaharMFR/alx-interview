#!/usr/bin/python3
""" Reads `stdin` line by line and computes metrics """
import sys
import re


standard = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - '
    r'\[(?P<date>[^\]]+)\] '
    r'"GET /projects/260 HTTP/1\.1" '
    r'(?P<status>\d{3}) '
    r'(?P<size>\d+)'
)

fileSize = 0
statusCount = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


def printStatistics():
    print("File size:", fileSize)
    for k, v in statusCount.items():
        if v != 0:
            print("{}: {}".format(k, v))


try:
    while True:
        for i in range(10):
            line = sys.stdin.readline()
            match = standard.match(line)
            if match is None:
                continue
            statusCount[match.group('status')] += 1
            fileSize += int(match.group('size'))
        printStatistics()
except KeyboardInterrupt:
    printStatistics()
    raise
