# -*- coding: utf-8 -*-
import csv
import glob
import json
from typing import Dict, List
import sys


folder = sys.argv[1]

def read_file(file_name: str) -> Dict:
  with open(file_name) as f:
    return json.load(f)


def extract_fields(data: Dict, fields: List[str]) -> List:
  row: List = []
  for field in fields:
    if field not in data and 'audits' in data:
      data = data['audits']
    if field in data:
      if 'rawValue' in data[field]:
        row.append(data[field]['rawValue'])
      else:
        row.append(data[field])
  return row


headers: List[str] = ['fetchTime', 'finalUrl', 'time-to-first-byte', 
                      'first-contentful-paint', 'first-meaningful-paint', 'speed-index',
                      'first-cpu-idle', 'interactive', 'total-byte-weight', 'file_name']

with open('reports/' + folder + '/summary.csv', 'w') as csv_file:
  writer = csv.writer(csv_file)
  writer.writerow(headers)

  for file_name in glob.glob('reports/' + folder + '/**/*.json'):
    data: Dict = read_file(file_name)
    row: List = extract_fields(data, headers)
    row.append(file_name)
    writer.writerow(row)
