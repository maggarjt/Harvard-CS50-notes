import csv
from sys import argv

if len(argv) !=3:
    print("Missing command line argument")
    exit(1)

with open(argv[1], newline='') as strfile:
    str_reader = csv.DictReader(strfile, delimiter =',')
    for col in str_reader:
       # print(",".join(row))
        print(col["name"], col["AGATC"], col["AATG"], col["TATC"] )


# raunning into issued undertsanding iteration of dictionaries and comparing dictionaries
#research in progress
