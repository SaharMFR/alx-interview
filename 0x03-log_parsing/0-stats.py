#!/usr/bin/python3
""" Reads `stdin` line by line and computes metrics """
import sys


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


def print_statistics():
    print("File size:", fileSize)
    for k, v in statusCount.items():
        if v != 0:
            print("{}: {}".format(k, v))


try:
    counter = 0
    for line in sys.stdin:
        if counter == 10:
            print_statistics()
            counter = 0
        data = line.split()
        fileSize += int(data[-1])
        statusCount[data[-2]] += 1
        counter += 1
except KeyboardInterrupt:
    print_statistics()
    raise
