# -*- coding: utf-8 -*-
import csv
import glob
import json

def read_file(file_name):
  with open(file_name) as f:
    return json.load(f)


def extract_fields(data, fields):
  row = []
  for field in fields:
    if field not in data and 'audits' in data:
      data = data['audits']
    if field in data:
      if 'rawValue' in data[field]:
        row.append(data[field]['rawValue'])
      else:
        row.append(data[field])
  return row


headers = ['fetchTime', 'finalUrl', 'first-contentful-paint', 
           'first-meaningful-paint', 'speed-index', 'time-to-first-byte',
           'first-cpu-idle', 'interactive', 'total-byte-weight', 'file_name']

with open('reports/summary.csv', 'w') as csv_file:
  writer = csv.writer(csv_file)
  writer.writerow(headers)

  for file_name in glob.glob('reports/**/*.json'):
    data = read_file(file_name)
    row = extract_fields(data, headers)
    row.append(file_name)
    writer.writerow(row)
