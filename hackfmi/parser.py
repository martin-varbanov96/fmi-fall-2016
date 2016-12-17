import csv
import json
import time

csvfile = open('Most+Recent+Cohorts+(Scorecard+Elements).csv', 'r')
headers_tmp=0
with open('Most+Recent+Cohorts+(Scorecard+Elements).csv', 'r') as f:
    for line in f:
       headers_tmp=line
       break
headers_tmp=headers_tmp.split(",")
headers=tuple(headers_tmp)
reader=list()
with open('Most+Recent+Cohorts+(Scorecard+Elements).csv', 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        reader.append(line.split(','))
json_file=open('json.json','w+')
for row in reader:
    print(row)
    json.dump(row, json_file)
    json_file.write('\n')