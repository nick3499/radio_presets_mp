#!/usr/bin/env python3
# license: MIT

from csv import reader  # CSV reader object
from subprocess import run  # execute args in CLI

urls = {}  # store: numerical keys/URL values

with open('stations_urls.csv', newline='') as file_obj:
    csv_read = reader(file_obj, delimiter=',')  # encoded wrapper
    print(f'{file_obj.readline()}')  # header (1st line of CSV file)
    c = 1  # initialize counter
    for rec in csv_read:
        print(f'{c:>2}: {rec[0]}')  # number/station
        urls[c] = rec[1]  # insert keys/values into `urls` dict
        c += 1  # increment counter

station_num = int(input('\x1b[1;36mEnter station number\x1b[0m: '))
# run(["mplayer", urls[station_num]])  # start mplayer
