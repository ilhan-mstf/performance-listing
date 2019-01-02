# -*- coding: utf-8 -*-
import glob
import json

def read_file(file_name):
  with open(file_name) as f:
    return json.load(f)


def extract_fields(data, fields):
  return []


headers = ["fetchTime", "finalUrl", "first-contentful-paint", "first-meaningful-paint", "speed-index", "time-to-first-byte", "first-cpu-idle", "interactive", "total-byte-weight"]

with open('reports/summary.csv', 'w') as csv_file:
  writer = csv_file.writer(csv_file)
  writer.writerow(headers)

  for file_name in glob.glob('reports/*.json'):
    data = read_file(file_name)
    row = extract_fields(data, headers)
    writer.writerow(row)
